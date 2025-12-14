# GitGrade AI 🚀

## Overview

GitGrade AI is an intelligent backend system that evaluates a student’s GitHub repository and converts it into a **Score**, **Summary**, and a **Personalized Improvement Roadmap**.

The goal of this project is to act as a **Repository Mirror** — reflecting the real strengths and weaknesses of a project exactly how a recruiter or mentor might see it.

This project was built as part of the **GitGrade Hackathon (AI + Code Analysis + Developer Profiling)**.

---

## ✨ Key Features

* Accepts **any public GitHub repository URL**
* Automatically fetches repository metadata using GitHub APIs
* Analyzes repository on multiple dimensions:

  * Project structure
  * README & documentation presence
  * Test presence
  * Commit consistency
* Generates:

  * **Numerical Score (0–100)**
  * **Skill Level** (Beginner / Intermediate / Advanced)
  * **Written Summary**
  * **Personalized Roadmap** with actionable steps

---

## 🧠 How It Works (Architecture)

1. **Input**: User provides a GitHub repository URL
2. **GitHub Fetcher**: Retrieves files, commits, and repo metadata
3. **Analyzer**: Evaluates structure, documentation, tests, and commits
4. **Scoring Engine**: Computes score, level, summary, and roadmap
5. **Output**: JSON response with complete evaluation

---

## 🛠️ Tech Stack

* **Python 3.12**
* **FastAPI** – Backend API
* **Uvicorn** – ASGI server
* **GitHub REST API** – Repository data

---

## 📂 Project Structure

```
backend/
│── app/
│   ├── main.py            # FastAPI entry point
│   ├── github_fetcher.py  # GitHub API integration
│   ├── analyzer.py        # Repository analysis logic
│   ├── scoring.py         # Scoring & roadmap engine
│── requirements.txt
│── venv/
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DiwanshiMathur2004/gitgrade-ai.git
cd gitgrade-ai/backend
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```
Optional: For interactive API testing, visit: http://127.0.0.1:8000/docs

---
🎥 Project Demo Video

The demo video of the project is available inside the video folder:
video/Project_Demo.mp4
## 🧪 API Usage

### 🔹 Grade a Repository

**Endpoint:**

```
POST /grade
```

**Example Request:**

```bash
POST http://127.0.0.1:8000/grade?repo_url=https://github.com/username/repository
```

**Sample Response:**

```json
{
  "repository": "username/repository",
  "score": 35,
  "level": "Beginner",
  "summary": "Project has a solid base but needs improvements.",
  "roadmap": [
    "Add unit or integration tests",
    "Improve project structure",
    "Commit more frequently"
  ]
}
```

---

## 🎯 Evaluation Criteria

* README presence
* Test coverage signals
* File organization
* Commit consistency

Scoring is intentionally **honest and actionable**, not inflated.

---

## 🔮 Future Improvements

* Language-specific code quality checks
* Cyclomatic complexity analysis
* CI/CD and GitHub Actions detection
* Frontend dashboard

---

## 🏁 Conclusion

GitGrade AI provides students with transparent, recruiter-style feedback on their GitHub repositories, helping them improve real-world coding practices and project readiness.

---

👩‍💻 **Author**: Diwanshi Mathur
🎓 Final Year B.Tech (Graduating April 2026)
