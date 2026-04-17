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

4. **Create PostgreSQL database:**
   ```bash
   createdb pokedex
   ```

## Running the Application

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Project Structure

- `main.py` - Main FastAPI application and route definitions
- `models.py` - SQLModel database models and schemas
- `database.py` - Database configuration and session management
- `config.py` - Application configuration from environment variables
- `requirements.txt` - Python dependencies

## Example API Usage

### Create a Pokémon
```bash
curl -X POST http://localhost:8000/pokemon \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Pikachu",
    "type": "Electric",
    "hp": 35,
    "attack": 55,
    "defense": 40
  }'
```

### Get all Pokémon
```bash
curl http://localhost:8000/pokemon
```

### Get a Pokémon by ID
```bash
curl http://localhost:8000/pokemon/1
```

### Update a Pokémon
```bash
curl -X PUT http://localhost:8000/pokemon/1 \
  -H "Content-Type: application/json" \
  -d '{
    "attack": 60
  }'
```

### Delete a Pokémon
```bash
curl -X DELETE http://localhost:8000/pokemon/1
```

## Environment Variables

See `.env.example` for all available configuration options.
