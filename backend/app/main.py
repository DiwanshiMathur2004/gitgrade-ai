from fastapi import FastAPI
from app.github_fetcher import get_repo_info
from app.analyzer import analyze_repository
from app.scoring import score_repository

app = FastAPI(title="GitGrade AI")

@app.post("/fetch")
def fetch_repo(repo_url: str):
    owner, repo = repo_url.split("/")[-2:]
    data = get_repo_info(owner, repo)
    return {
        "repository": data["full_name"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"]
    }

@app.post("/analyze")
def analyze(repo_url: str):
    owner, repo = repo_url.split("/")[-2:]
    analysis = analyze_repository(owner, repo)
    return {
        "repository": f"{owner}/{repo}",
        "analysis": analysis
    }

@app.post("/grade")
def grade(repo_url: str):
    owner, repo = repo_url.split("/")[-2:]
    analysis = analyze_repository(owner, repo)
    score_data = score_repository(analysis)

    return {
        "repository": f"{owner}/{repo}",
        **score_data
    }

