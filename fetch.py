
import os
from github import Github

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise EnvironmentError("GITHUB_TOKEN environment variable not set.")
g = Github(token)

repo_owner = "wyattx05"
repo_name = "test-repo"

try:
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    # Fetch all open issues
    issues = repo.get_issues(state='open')

    print(f"Open issues in {repo_owner}/{repo_name}:")
    for issue in issues:
        print(f"  Issue #{issue.number}: {issue.title} (Created by: {issue.user.login})")
except Exception as e:
    print(f"An error occurred: {e}")
