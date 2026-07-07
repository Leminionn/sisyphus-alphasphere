# OptiBot Mini-Clone (Take-Home Test)

A lightweight, robust Data Synchronization Pipeline (ETL) designed to sync support articles from `support.optisigns.com` directly to a Google Gemini File Search Store (Vector Store equivalent) for Retrieval-Augmented Generation (RAG).

---

## 🛠 Setup

### Prerequisites
- Python 3.12+
- Google Gemini API Key

### Local Installation

1. **Clone the repository** (use a cryptic name for privacy).
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```bash
   cp .env.sample .env
   ```
   Open `.env` and enter your `GEMINI_API_KEY`.

---

## 🚀 How to Run Locally

Run the pipeline execution command:
```bash
python main.py
```
Upon running:
1. The scraper fetches public articles from `support.optisigns.com` (no credentials required).
2. Converts raw HTML content into clean Markdown files saved under `data/articles/en-us/<slug>.md`.
3. Performs delta detection via SHA-256 content hashing.
4. Programmatically initializes and uploads/indexes new or updated markdown files to the Google Gemini `file_search_stores` RAG knowledge base.
5. Deletes local and remote documents for deleted support articles.

---

## 🐋 Running via Docker

### Build the Image
```bash
docker build -t optibot-sync-pipeline .
```

### Run the Container
Pass your `API_KEY` (or `GEMINI_API_KEY`) as an environment variable:
```bash
docker run --rm -e API_KEY="your_api_key_here" optibot-sync-pipeline
```

---

## 🧠 Chunking Strategy & Vector Store

We leverage Gemini's managed **File Search Stores** for RAG.
- **Managed Pipeline**: File ingestion, semantic embeddings, and vector indexing are handled automatically by Google's backend.
- **Chunking Strategy**: We delegate chunking to Gemini's native managed File Search Store indexing pipeline. This automatically parses the Markdown document, preserving structural blocks (headings, paragraphs, lists, tables) to maintain context and optimize retrieval search relevance.
- **Grounding & Citations**: The AI model uses the File Search Store tool directly, producing grounded answers with automated article citations.

---

## ☁️ Daily Job Scheduling (GitHub Actions)

Deploy the scraper on any platform or run it as a daily cron job via GitHub Actions.
Workflow details are configured in `.github/workflows/daily-sync.yml` to preserve `data/state.json` sync cache between runs:

```yaml
name: Daily OptiBot Data Sync

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run ETL Pipeline
        env:
          API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python main.py

      - name: Commit and Push state changes
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add data/state.json data/articles/
          git diff --quiet && git diff --staged --quiet || (git commit -m "chore: update sync state [skip ci]" && git push)
```

- **Daily Job Logs**: [Link to GitHub Actions Run Logs](https://github.com/your-username/your-repo-name/actions)

---

## 📸 Sanity Check Screenshot

Ask the Assistant in Google AI Studio / OpenAI Playground: **"How do I add a YouTube video?"**
Include your screenshot showing correct answer and citations here:

![Assistant Sanity Check Response](docs/assets/assistant-response.png)
