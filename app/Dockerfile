
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Increase pip timeout to handle slow network connections
RUN python -m pip install \
    --no-cache-dir \
    --timeout 120 \
    --retries 10 \
    -r requirements.txt

COPY app.py .

RUN useradd --create-home --uid 10001 appuser

USER appuser

EXPOSE 5252

CMD ["gunicorn", "--bind", "0.0.0.0:5252", \
     "--workers", "2", "--access-logfile", "-", \
     "app:app"]
