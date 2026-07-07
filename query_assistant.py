#!/usr/bin/env python
"""
OptiBot RAG CLI Assistant Query Tool.
Supports both single question queries and interactive terminal chat sessions.
"""

import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

load_dotenv()

def get_gemini_client():
    """Initializes and returns the Google GenAI client."""
    api_key = os.environ.get("API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY is not configured. Please add it to your .env file.")
        sys.exit(1)
    return genai.Client(api_key=api_key)

def find_store_name(client, display_name: str) -> str:
    """Finds the full resource name of the File Search Store by its display name."""
    try:
        stores = client.file_search_stores.list()
        for store in stores:
            if store.display_name == display_name:
                return store.name
        return None
    except APIError as e:
        print(f"[ERROR] Failed to query Gemini stores: {e}")
        sys.exit(1)

def query_rag_assistant(client, store_resource_name: str, question: str, show_citations: bool = False):
    """Sends a query to the Gemini model grounded with the File Search Store."""
    sys_instruction = (
        "You are OptiBot, the customer-support bot for OptiSigns.com.\n"
        "• Tone: helpful, factual, concise.\n"
        "• Only answer using the uploaded docs.\n"
        "• Max 5 bullet points; else link to the doc.\n"
        "• Cite up to 3 'Article URL:' lines per reply."
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=sys_instruction,
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[store_resource_name]
                        )
                    )
                ]
            )
        )
        
        print("\n[OptiBot]:")
        print(response.text)
        
        # Display citation metadata if requested
        if show_citations and response.candidates and response.candidates[0].grounding_metadata:
            metadata = response.candidates[0].grounding_metadata
            if metadata.grounding_chunks:
                print("\n[Citations]:")
                for idx, chunk in enumerate(metadata.grounding_chunks, start=1):
                    if chunk.web and chunk.web.uri:
                        print(f"  [{idx}] Web Source: {chunk.web.uri}")
                    elif chunk.retrieved_context:
                        ctx = chunk.retrieved_context
                        title_str = f" ({ctx.title})" if ctx.title else ""
                        print(f"  [{idx}] Document: {ctx.uri}{title_str}")
            else:
                print("\n[Citations]: No source citations returned.")
        print("-" * 50)
        
    except APIError as e:
        print(f"\n[ERROR] Gemini API error: {e}")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

BANNER = """
 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗ ███████╗██████╗ ██╗  ██╗███████╗██████╗ ███████╗
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗██╔════╝██╔══██╗██║  ██║██╔════╝██╔══██╗██╔════╝
███████║██║     ██████╔╝███████║███████║███████╗██████╔╝███████║█████╗  ██████╔╝█████╗  
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║╚════██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗██╔══╝  
██║  ██║███████╗██║     ██║  ██║██║  ██║███████║██║     ██║  ██║███████╗██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝

               RAG Chat Assistant for OptiBot Mini-Clone
"""

def start_interactive_session(client, store_resource_name: str, show_citations: bool):
    """Launches an interactive shell chat loop with the assistant."""
    print(BANNER)
    print("=" * 60)
    print("  Type 'exit', 'quit', or 'q' to end the chat session.")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Goodbye!")
                break
            
            query_rag_assistant(client, store_resource_name, user_input, show_citations)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

def main():
    parser = argparse.ArgumentParser(description="Query the RAG-grounded OptiBot Assistant via command-line.")
    parser.add_argument(
        "-q", "--question",
        type=str,
        help="A single question to ask OptiBot. If omitted, starts an interactive chat loop."
    )
    parser.add_argument(
        "-s", "--store",
        type=str,
        default=os.environ.get("GEMINI_STORE_NAME", "optibot-knowledge-base"),
        help="Display name of the Gemini File Search Store (default: optibot-knowledge-base)."
    )
    parser.add_argument(
        "-c", "--citations",
        action="store_true",
        help="Show raw grounding citation source files returned by the Gemini API."
    )
    
    args = parser.parse_args()
    
    client = get_gemini_client()
    
    # Locate store
    store_resource_name = find_store_name(client, args.store)
    if not store_resource_name:
        print(f"[ERROR] Gemini File Search Store with display_name '{args.store}' was not found.")
        print("Please run 'python main.py' first to initialize the store and upload documents.")
        sys.exit(1)
        
    # Execute query or start loop
    if args.question:
        query_rag_assistant(client, store_resource_name, args.question, args.citations)
    else:
        start_interactive_session(client, store_resource_name, args.citations)

if __name__ == "__main__":
    main()
