# OptiBot Data Synchronization Pipeline (ETL)

A robust, modular, and OOP-designed Python ETL pipeline built for **OptiBot** (an AI Support Bot). The pipeline extracts Help Center articles from the Zendesk API, converts the HTML content to clean Markdown with metadata, detects changes (additions, updates, and deletions), and uploads the files to the Google Gemini File API using the official modern `google-genai` SDK.

---

## Features

- **Zendesk API Extraction**: Automatically paginates and extracts published articles (skipping drafts) for configured locales.
- **Markdown Conversion**: Uses `markdownify` to convert HTML bodies into clean Markdown and prepends essential metadata (Article ID, Locale, Last Updated) for the AI model's context.
- **Delta Detection**: Computes SHA-256 hashes of Markdown files and tracks synchronization state in `data/state.json`. Only uploads added/updated articles and handles remote deletions.
- **Modern Gemini SDK Integration**: Integrates the new `google-genai` SDK, leveraging the File API to handle uploads and remote file deletion.
- **Dockerized**: Easy-to-deploy Docker image.
- **Secrets Management**: Configuration via `config.yaml` or direct overrides via Environment Variables.

---

## Directory Structure

```text
optibot-sync-pipeline/
├── main.py              # CLI entry point
├── config.yaml          # Local settings configuration
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container configuration
├── README.md            # Setup and deployment documentation
├── .gitignore           # Ignored files for Git
├── data/                # Local data storage (synced articles and state)
│   ├── articles/        # Synced markdown articles sorted by locale
│   └── state.json       # Pipeline sync state log
└── src/
    ├── core/
    │   ├── pipeline.py  # Orchestrates ETL pipeline steps
    │   ├── config.py    # Loads config with Env overrides
    │   └── models.py    # Article and state dataclasses
    ├── extract/
    │   └── zendesk.py   # Extract helper for Zendesk API
    ├── transform/
    │   └── markdown.py  # Converts HTML body to markdown + metadata
    ├── load/
    │   └── gemini.py    # File API uploads/deletions with google-genai
    ├── delta/
    │   └── detector.py  # Handles state persistence & delta checks
    └── utils/
        ├── hash.py      # Computes SHA-256 hex string
        └── logger.py    # Set up stdout logs formatting
```

---

## Setup & Local Execution

### Step 0: Set Up a Virtual Environment (Windows)

Open your terminal (PowerShell or Command Prompt) in the project root directory and run:

```powershell
# Create the virtual environment
python -m venv venv

# Activate on PowerShell
.\venv\Scripts\Activate.ps1

# Or Activate on Command Prompt
.\venv\Scripts\activate.bat
```

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure the Application

Edit the `config.yaml` file with your details:

```yaml
zendesk:
  subdomain: "your-subdomain"
  email: "your-email@example.com"
  token: "your-zendesk-api-token"
  locales: ["en-us"] # Specify locales to sync

gemini:
  api_key: "your-gemini-api-key"
  model: "gemini-2.5-flash"

pipeline:
  data_dir: "data"
  articles_dir: "data/articles"
  state_file: "data/state.json"
```

> [!TIP]
> You can leave API keys/tokens empty in `config.yaml` and export them as environment variables instead:
> - `ZENDESK_SUBDOMAIN`
> - `ZENDESK_EMAIL`
> - `ZENDESK_TOKEN`
> - `GEMINI_API_KEY`

### Step 3: Run the Pipeline

```bash
python main.py
```

---

## Running with Docker

You can containerize the application to run it in isolated environments.

### Build the Image
```bash
docker build -t optibot-sync-pipeline .
```

### Run the Image
Map a local directory to `/app/data` to ensure that `state.json` and local markdown cache files persist between sync executions.

```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  -e ZENDESK_SUBDOMAIN="your-subdomain" \
  -e ZENDESK_EMAIL="your-email@example.com" \
  -e ZENDESK_TOKEN="your-zendesk-api-token" \
  -e GEMINI_API_KEY="your-gemini-api-key" \
  optibot-sync-pipeline
```

---

## Daily Schedule via GitHub Actions

To run this pipeline daily, configure a GitHub Actions workflow that utilizes GitHub Cache to persist `state.json` and local markdown articles.

Create a file named `.github/workflows/daily-sync.yml` with the following content:

```yaml
name: Daily OptiBot Data Sync

on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily at midnight UTC
  workflow_dispatch:      # Allows manual trigger via GitHub UI

jobs:
  sync:
    runs-on: ubuntu-latest
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

      - name: Restore cache state
        id: cache-state
        uses: actions/cache@v4
        with:
          path: data/
          key: optibot-state-${{ github.run_id }}
          restore-keys: |
            optibot-state-

      - name: Run ETL Pipeline
        env:
          ZENDESK_SUBDOMAIN: ${{ secrets.ZENDESK_SUBDOMAIN }}
          ZENDESK_EMAIL: ${{ secrets.ZENDESK_EMAIL }}
          ZENDESK_TOKEN: ${{ secrets.ZENDESK_TOKEN }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GEMINI_MODEL: "gemini-2.5-flash"
        run: python main.py

      # Save state back to GitHub Cache for the next run
      - name: Save cache state
        if: always()
        uses: actions/cache/save@v4
        with:
          path: data/
          key: optibot-state-${{ github.run_id }}
```

### Adding Secrets to GitHub

Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions** and add the following repository secrets:
1. `ZENDESK_SUBDOMAIN`: Your Zendesk subdomain (e.g., `company` from `company.zendesk.com`).
2. `ZENDESK_EMAIL`: Your Zendesk agent login email.
3. `ZENDESK_TOKEN`: Your Zendesk API Token.
4. `GEMINI_API_KEY`: Your Google Gemini API Key.
