# -------------------------
# Stage 1 – Builder
# -------------------------
FROM python:3.12-slim AS builder

WORKDIR /install

# Copy dependency file
COPY req.txt .

# Install dependencies into a custom path
RUN pip install --no-cache-dir --prefix=/install -r req.txt


# -------------------------
# Stage 2 – Runtime
# -------------------------
FROM python:3.12-slim

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY app ./app

# Expose FastAPI port
EXPOSE 8000

# Run the app (dev-style with reload)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
