# Resume vs Job Description Matcher

A Django web app that compares a resume with a job description, scores the match, and shows which skills are missing, with a tip for each gap.

## Features
- Paste resume text or upload a PDF/DOCX resume
- Skill-based match score with a progress bar
- Matched and missing skills
- Suggestions for closing each skill gap
- History of past checks with detail view and delete
- Form validation and error messages

## Tech stack
Python, Django, SQLite, Bootstrap, pypdf, python-docx

## How it works
1. The resume text is read from the form, or extracted from the uploaded file.
2. Both texts are scanned for skills from a fixed skill list (with aliases such as "Postgres" for PostgreSQL).
3. Score = matched skills / skills required by the job x 100.
4. Each missing skill gets a suggestion on how to build it into a project.

## Run locally
    git clone <your-repo-url>
    cd resume-matcher
    python -m venv venv
    venv\Scripts\activate
    pip install django pypdf python-docx
    python manage.py migrate
    python manage.py runserver

## Limitations
- Matching uses a fixed skill list, so skills outside the list are ignored.
- Scanned (image-only) PDFs can't be read.

## Screenshots
(add screenshots here)

## Live demo
(https://resume-matcher-sjjq.onrender.com/)
