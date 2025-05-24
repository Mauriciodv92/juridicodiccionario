FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pymupdf pymongo \
    && pip install pytest flask pymongo \
    && pip install pytest



EXPOSE 5000

CMD ["python", "app.py"]

