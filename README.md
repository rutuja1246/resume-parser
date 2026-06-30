#  Resume Parser ATS

An AI-powered Resume Parser and Applicant Tracking System (ATS) built using Flask, PostgreSQL, Regex, and spaCy. The application automatically extracts key candidate information from PDF and DOCX resumes, stores it in a PostgreSQL database, and provides an intuitive dashboard for HR professionals to search and manage applicants.

---

## Features

### Candidate Portal
- Resume upload (PDF & DOCX)
- Automatic resume parsing
- Success notification after submission

### Employee Dashboard
- Search candidates by name, degree, or skills
- View detailed candidate profiles
- Delete candidate records
- Direct email integration (Gmail compose)
- Total candidate count

### Resume Parsing
- Name extraction
- Email extraction
- Phone number extraction
- Skills extraction
- Education extraction
- PDF and DOCX support

### Database
- PostgreSQL integration
- Automatic storage of parsed information
- Searchable candidate database

---

## Tech Stack

### Backend
- Python
- Flask
- PostgreSQL
- psycopg2

### Resume Parsing
- spaCy
- Regex
- pdfplumber
- python-docx

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

---

## Project Structure

```text
ResumeParser/
│
├── app.py
├── database.py
├── config.py
├── requirements.txt
│
├── parser/
│   ├── extract_name.py
│   ├── extract_email.py
│   ├── extract_phone.py
│   ├── extract_skills.py
│   ├── extract_education.py
│   ├── pdf_parser.py
│   └── docx_parser.py
│
├── templates/
│   ├── landing.html
│   ├── index.html
│   ├── dashboard.html
│   └── candidate.html
│
├── static/
│   └── css/
│       └── style.css
│
└── uploads/
```

## ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project

```bash
cd ResumeParser
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure PostgreSQL

- Create a PostgreSQL database.
- Update `config.py` with your database credentials.

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

## 📸 Screenshots

### Landing Page

<img width="1917" height="1017" alt="landing-page" src="https://github.com/user-attachments/assets/d2030f79-95c5-49fa-ae13-e3f74448ef0b" />

### Candidate Portal

<img width="1912" height="1012" alt="apply" src="https://github.com/user-attachments/assets/79659291-cc73-4c46-8d1b-84618e3cb31c" />

### Employee Dashboard

<img width="1917" height="1017" alt="dashboard" src="https://github.com/user-attachments/assets/38f924fc-3f91-4fd3-a34d-76f0851365cb" />

### Candidate Profile

<img width="1917" height="1017" alt="candidate-profile" src="https://github.com/user-attachments/assets/64501697-9a3c-4939-a352-e6da87fc00a5" />

---

## 🔍 Workflow

Landing Page
        │
        ├───────────────┐
        │               │
        ▼               ▼
 Candidate         Employee
    │                  │
    ▼                  ▼
Upload Resume      Dashboard
    │                  │
    ▼                  ▼
Resume Parsing     Search Candidates
    │                  │
    ▼                  ▼
PostgreSQL        View/Delete Candidate
```

## 👩‍💻 Author

**Rutuja Chavan**

Computer Science Engineering (AI & ML)

Mumbai, India

GitHub: https://github.com/rutuja1246

LinkedIn: https://linkedin.com/in/rutujachavan0430

---

## 📜 License

This project is developed for educational purposes.
