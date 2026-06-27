import re

import spacy

nlp = spacy.load("en_core_web_sm")

from parser.skills import SKILLS

from parser.education import (
    DEGREES,
    INSTITUTION_KEYWORDS,
    FIELD_KEYWORDS
)


def extract_email(text):
    """
    Extract email from resume text.
    """

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    matches = re.findall(pattern, text)

    if matches:
        return matches[0]

    return None

def extract_phone(text):
    """
    Extract phone number from resume text.
    """

    pattern = r"(?:\+91)?\s?\d{10}"

    matches = re.findall(pattern, text)

    if matches:
        return matches[0]

    return None

def extract_name(text):
    """
    Extract candidate name using heuristics first,
    then fall back to spaCy.
    """

    lines = text.split("\n")

    ignore_words = {
        "summary",
        "skills",
        "education",
        "experience",
        "projects",
        "certifications",
        "github",
        "linkedin",
        "email",
        "phone",
        "engineer",
        "developer",
        "student"
    }

    # Only inspect the top of the resume
    for line in lines[:10]:

        line = line.strip()

        if not line:
            continue

        # Skip emails
        if "@" in line:
            continue

        # Skip numbers
        if any(char.isdigit() for char in line):
            continue

        # Skip unwanted keywords
        if any(word in line.lower() for word in ignore_words):
            continue

        words = line.split()

        # Candidate names are usually 2-4 words
        if 2 <= len(words) <= 4:

            # Every word should contain only letters
            if all(word.replace(".", "").isalpha() for word in words):
                return line.title()

    # ---------- Fallback to spaCy ----------

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None


def extract_skills(text):
    """
    Extract technical skills from resume text.
    """

    found_skills = set()

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.add(skill)

    return sorted(found_skills)


def extract_education(text):

    education = {
        "degree": None,
        "institution": None,
        "field": None
    }

    # Degree
    for degree in DEGREES:

        pattern = r"\b" + re.escape(degree) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            education["degree"] = degree
            break

    # Institution
    lines = text.split("\n")

    for line in lines:

        for keyword in INSTITUTION_KEYWORDS:

            if keyword.lower() in line.lower():

                education["institution"] = line.strip()
                break

        if education["institution"]:
            break

    # Field
    for field in FIELD_KEYWORDS:

        pattern = r"\b" + re.escape(field) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):

            education["field"] = field
            break

    return education

def extract_information(text):
    """
    Extract all candidate information.
    """

    candidate = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text)
    }

    return candidate