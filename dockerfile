FROM python:3.10-slim

WORKDIR /app

COPY . /app

ENV DEBIAN_FRONTEND=noninteractive

# Update package lists
RUN apt-get update

# Install dependencies one group at a time
RUN apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libtesseract-dev

RUN apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libfontconfig1

RUN apt-get install -y --no-install-recommends \
    default-jre \
    poppler-utils

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]