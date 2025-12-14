from app.github_fetcher import get_repo_files, get_repo_commits

def analyze_repository(owner: str, repo: str):
    files = get_repo_files(owner, repo)
    commits = get_repo_commits(owner, repo)

    has_readme = any(f["name"].lower() == "readme.md" for f in files)
    has_tests = any("test" in f["name"].lower() for f in files)

    return {
        "total_files": len(files),
        "has_readme": has_readme,
        "has_tests": has_tests,
        "total_commits": len(commits)
    }
