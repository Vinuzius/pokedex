# Pokédex API

A FastAPI + SQLModel + PostgreSQL template application.

## Prerequisites

- Python 3.10+
- PostgreSQL 12+

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your PostgreSQL connection details
   ```


## Running the Application

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload
```

Or with Fastapi:
```bash fastapi run ``

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Project Structure

- `main.py` - Main FastAPI application and route definitions
- `models.py` - SQLModel database models and schemas
- `database.py` - Database configuration and session management
- `requirements.txt` - Python dependencies

## Example API Usage

```configurando ```

## Environment Variables

See `.env.example` for all available configuration options.
