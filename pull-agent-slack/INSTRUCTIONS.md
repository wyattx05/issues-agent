# Setup Instructions for fetch.py

This script fetches open issues from a GitHub repository, summarizes them using OpenAI's GPT, and sends the summaries to Slack via a webhook.

## Prerequisites

- Python 3.7 or higher (a virtual environment is recommended)
- The following Python packages:
  - `PyGithub`
  - `requests`

## Installation

1. **Clone the repository or copy the script to your machine.**

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install PyGithub requests
   ```

## Environment Variables

Before running the script, set the following environment variables in your terminal:

- `GITHUB_TOKEN`: Your GitHub personal access token (with repo access)
- `OPENAI_API_KEY`: Your OpenAI API key
- `SLACK_WEBHOOK_URL`: Your Slack Incoming Webhook URL

Example (replace with your actual values):
```sh
export GITHUB_TOKEN=your_github_token
export OPENAI_API_KEY=your_openai_api_key
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
```

You can add these lines to your `.zshrc` or `.bashrc` to set them automatically in new terminal sessions.

## Running the Script

From the project directory, run:
```sh
python fetch.py
```

If using a virtual environment, make sure it is activated before running the script.

---

If you have any issues, ensure your environment variables are set and dependencies are installed.
