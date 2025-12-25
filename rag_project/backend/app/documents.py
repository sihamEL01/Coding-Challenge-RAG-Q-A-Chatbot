# backend/app/documents.py
import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into chunks of `chunk_size` words with `overlap` words overlapping.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    pdf_path ="D:/quorium project/rag_project/Schatzinsel_E.pdf"
  # replace with your PDF
    if not os.path.exists(pdf_path):
        print(f"PDF not found at {pdf_path}")
    else:
        text = extract_text_from_pdf(pdf_path)
        chunks = chunk_text(text)
        print(f"Extracted {len(chunks)} chunks from PDF")
