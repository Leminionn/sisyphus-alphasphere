FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY main.py .

RUN mkdir -p data

VOLUME [ "/app/data" ]

ENTRYPOINT [ "python", "main.py" ]
