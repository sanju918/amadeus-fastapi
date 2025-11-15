# FastAPI with UV

A FastAPI project using UV as the package manager.

## Setup

1. Make sure you have Python 3.8+ installed
2. Install UV if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

## Installation

1. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

## Running the application

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

## API Documentation

- Interactive API docs: http://127.0.0.1:8000/docs
- Alternative API docs: http://127.0.0.1:8000/redoc
- Health check: http://127.0.0.1:8000/health
