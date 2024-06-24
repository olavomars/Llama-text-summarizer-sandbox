from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(pdf_file: io.BytesIO) -> str:
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

