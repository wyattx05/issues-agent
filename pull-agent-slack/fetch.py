import os
import requests
from github import Github


# Load environment variables
token = os.getenv("GITHUB_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")
slack_webhook = os.getenv("SLACK_WEBHOOK_URL")


if not token:
    raise EnvironmentError("GITHUB_TOKEN environment variable not set.")
if not slack_webhook:
    raise EnvironmentError("SLACK_WEBHOOK_URL environment variable not set.")

g = Github(token)

repo_owner = "wyattx05"
repo_name = "test-repo"


def summarize_issue(title, body):
    if not openai_key:
        # If no OpenAI key, return a dummy summary for testing
        return "[Test Mode] No OpenAI key set. This is a placeholder summary."
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai_key}",
        "Content-Type": "application/json"
    }
    prompt = f"Summarize the following GitHub issue in 2-3 sentences for a Slack update.\nTitle: {title}\nBody: {body}"
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes GitHub issues for Slack."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    summary = response.json()["choices"][0]["message"]["content"].strip()
    return summary

def send_to_slack(text):
    payload = {"text": text}
    resp = requests.post(slack_webhook, json=payload)
    resp.raise_for_status()

try:
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    issues = repo.get_issues(state='open')

    print(f"Open issues in {repo_owner}/{repo_name}:")
    for issue in issues:
        print(f"  Issue #{issue.number}: {issue.title} (Created by: {issue.user.login})")
        body = issue.body or "No description."
        summary = summarize_issue(issue.title, body)
        slack_message = f"*Issue #{issue.number}:* {issue.title}\n_Summary:_ {summary}\n_Created by:_ {issue.user.login}"
        send_to_slack(slack_message)
        print(f"  -> Sent summary to Slack.")
except Exception as e:
    print(f"An error occurred: {e}")
