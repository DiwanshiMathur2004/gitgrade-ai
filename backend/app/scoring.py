def score_repository(analysis: dict):
    score = 0
    roadmap = []

    # README
    if analysis["has_readme"]:
        score += 20
    else:
        roadmap.append("Add a detailed README with setup and usage instructions")

    # Tests
    if analysis["has_tests"]:
        score += 25
    else:
        roadmap.append("Add unit or integration tests to improve reliability")

    # File structure
    if analysis["total_files"] >= 5:
        score += 20
    else:
        roadmap.append("Improve project structure by adding more modular files")

    # Commit quality
    if analysis["total_commits"] >= 5:
        score += 20
    else:
        roadmap.append("Commit more frequently with meaningful messages")

    # Baseline
    score += 15

    # Level
    if score >= 80:
        level = "Advanced"
    elif score >= 50:
        level = "Intermediate"
    else:
        level = "Beginner"

    summary = (
        "Project has a solid base but needs improvements."
        if score < 80
        else "Project is well-structured and close to production quality."
    )

    return {
        "score": score,
        "level": level,
        "summary": summary,
        "roadmap": roadmap
    }
