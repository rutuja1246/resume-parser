from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from parser.extractor import extract_text

from parser.info_extractor import extract_information

from database import save_candidate, get_all_candidates

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

        save_candidate(candidate)

        for key, value in candidate.items():
            print(f"{key.title()}: {value}")
        

        return f"{filename} uploaded and parsed successfully!"

    return "Invalid file type. Please upload a PDF or DOCX."

@app.route("/dashboard")
def dashboard():

    candidates = get_all_candidates()

    return render_template(
        "dashboard.html",
        candidates=candidates
    )



if __name__ == "__main__":
    app.run(debug=True)