from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io
import os

app = FastAPI()

# Set the path to Tesseract-OCR executable
# pytesseract.pytesseract.tesseract_cmd = "D:\\256SSD\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD', '/usr/bin/tesseract')

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    try:
        # Read image file
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes))
        
        # Convert image to text
        text = pytesseract.image_to_string(img)
        
        return {"extracted_text": text}
    except Exception as e:
        return {"error": str(e)}