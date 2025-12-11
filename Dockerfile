# Build Stage
FROM python:3.12-slim AS builder

WORKDIR /install

COPY requirement.txt .

# Install dependencies into a custom path
RUN pip install --no-cache-dir --prefix=/install -r requirement.txt

# Run Stage
FROM python:3.12-slim

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

COPY app ./app
COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic
COPY entrypoint.sh /app/entrypoint.sh
EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]
