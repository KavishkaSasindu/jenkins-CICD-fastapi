#!/bin/bash

set -o

echo "Runing alembic migrations..."
alembic upgrade head

echo "Starting the FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
