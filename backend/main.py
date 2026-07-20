from fastapi import FastAPI, UploadFile, File
import shutil
import os

from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text
from parser.txt_parser import extract_txt_text


app = FastAPI(
    title="AI Test Automation Framework"
)


@app.get("/")
def home():
    return {
        "message": "Framework Running"
    }



@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = f"docs/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )


    if file.filename.endswith(".pdf"):
        text = extract_pdf_text(file_path)

    elif file.filename.endswith(".docx"):
        text = extract_docx_text(file_path)

    elif file.filename.endswith(".txt"):
        text = extract_txt_text(file_path)

    else:
        return {
            "error": "Unsupported file"
        }


    return {
        "filename": file.filename,
        "text": text
    }