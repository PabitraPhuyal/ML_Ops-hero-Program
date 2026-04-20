FROM python:3.11-slim@sha256:a1a5797e590e4a1e1d5b2e5d8c7e6f5a4b3c2d1e0f1a2b3c4d5e6f7a8b9c0d

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
ENV PORT=8000

# Unprivileged user
RUN useradd -m runner
USER runner

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
