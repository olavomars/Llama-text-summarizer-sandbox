from fastapi import FastAPI, File, UploadFile
from pdf_processor import extract_text_from_pdf
from summarizer import initialize_llama, summarize_text
import io

app = FastAPI()
llm = initialize_llama()

@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    pdf_file = io.BytesIO(await file.read())
    text = extract_text_from_pdf(pdf_file)
    summary = summarize_text(llm, text)
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

