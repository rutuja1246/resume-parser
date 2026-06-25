import os

from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        return None