import requests

GITHUB_API_BASE = "https://api.github.com"

def get_repo_info(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url)
    return response.json()

def get_repo_files(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents"
    response = requests.get(url)
    return response.json()

def get_repo_commits(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    return response.json()
