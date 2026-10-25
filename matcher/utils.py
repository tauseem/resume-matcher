import re

SKILLS = {
    "python", "java", "javascript", "c++", "c#", "sql",
    "django", "flask", "fastapi", "django rest framework", "rest api",
    "mysql", "postgresql", "sqlite", "mongodb", "redis",
    "pandas", "numpy", "matplotlib", "machine learning", "data analysis",
    "html", "css", "bootstrap", "react", "angular", "json", "ajax",
    "git", "github", "docker", "aws", "linux", "celery",
    "oop", "data structures", "algorithms", "authentication", "jwt",
    "unit testing", "pytest", "debugging", "agile",
}

ALIASES = {
    "rest apis": "rest api",
    "restful": "rest api",
    "drf": "django rest framework",
    "postgres": "postgresql",
    "object-oriented": "oop",
    "object oriented": "oop",
    "dsa": "data structures",
}

TIPS = {
    "docker": "Containerize one of your projects with a Dockerfile, then list it under that project.",
    "aws": "Deploy a project on AWS (EC2 or Elastic Beanstalk free tier) and add the live link.",
    "celery": "Add a background task to a project, such as sending an email, using Celery with Redis.",
    "redis": "Use Redis for caching or as the Celery broker in a project.",
    "unit testing": "Write tests for your views and utils using Django's test framework, then mention the coverage.",
    "pytest": "Write a few tests with pytest for your utility functions.",
    "django rest framework": "Build a small REST API with DRF and list the endpoints in your README.",
    "rest api": "Build and document a REST API, and test it in Postman.",
    "react": "Build a small front end in React that calls one of your APIs.",
    "mongodb": "Build a small project that stores its data in MongoDB.",
    "linux": "Learn basic Linux commands and deploy a project on a Linux server.",
    "jwt": "Add JWT token login to one of your APIs.",
    "agile": "Mention how you plan and track work, for example with a Trello or GitHub Projects board.",
    "fastapi": "Rebuild one small API with FastAPI to learn the differences from Django.",
    "machine learning": "Do one small project with scikit-learn, such as a prediction model, and publish it on GitHub.",
}

DEFAULT_TIP = "Learn the basics and build one small project that uses it, then add it to your resume."


def find_skills(text):
    text = text.lower()
    for alias, standard in ALIASES.items():
        text = re.sub(r"(?<![a-z0-9+#])" + re.escape(alias) + r"(?![a-z0-9+#])", standard, text)

    found = set()
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"
        if re.search(pattern, text):
            found.add(skill)
    return found


def analyze(resume_text, job_description):
    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)

    if not job_skills:
        return {"score": 0, "matched": [], "missing": [], "suggestions": []}

    matched = job_skills & resume_skills
    missing = job_skills - resume_skills
    score = round(len(matched) / len(job_skills) * 100, 1)

    suggestions = [
        {"skill": skill, "tip": TIPS.get(skill, DEFAULT_TIP)}
        for skill in sorted(missing)
    ]

    return {
        "score": score,
        "matched": sorted(matched),
        "missing": sorted(missing),
        "suggestions": suggestions,
    }