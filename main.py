from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


ALLOWED_ORIGINS = [
    "http://localhost:3000",                 # your Next.js dev
    "https://imagetotext-hp54.onrender.com", # your API origin itself (safe)
    "https://ycap.in", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,           # set True only if you need cookies/auth
    allow_methods=["POST", "OPTIONS"], # OPTIONS is important for preflight
    allow_headers=["*"],
)


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
        text = pytesseract.image_to_string(img, config="--oem 1 --psm 6")
        
        return {"extracted_text": text}
    except Exception as e:
        return {"error": str(e)}