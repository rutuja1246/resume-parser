from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from parser.extractor import extract_text

from parser.info_extractor import extract_information

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return "No file selected"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        text = extract_text(filepath)

        candidate = extract_information(text)

        print("RAW EXTRACTED TEXT")
        print("=" * 60)
        print(text)

        print("=" * 60)
        print("EXTRACTED INFORMATION")
        print("=" * 60)

        print("=" * 60)
        print("EDUCATION SECTION")
        print("=" * 60)

        for key, value in candidate.items():
            print(f"{key.title()}: {value}")
        

        return f"{filename} uploaded and parsed successfully!"

    return "Invalid file type. Please upload a PDF or DOCX."



if __name__ == "__main__":
    app.run(debug=True)