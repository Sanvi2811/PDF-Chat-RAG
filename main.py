from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    msg = process_pdf(file_path)
    os.remove(file_path)  # optional cleanup
    return {"message": msg}

@app.post("/ask/")
async def ask(query: dict):
    answer = ask_question(query["question"])
    return {"answer": answer}
