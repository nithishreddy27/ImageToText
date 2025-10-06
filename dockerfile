FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    default-jre \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]