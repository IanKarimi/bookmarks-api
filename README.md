# Bookmarks API

A small REST API for saving and searching bookmarks, built with FastAPI, SQLAlchemy and SQLite.

## Features

- Create, read, update and delete bookmarks
- Input validation with Pydantic (invalid URLs are rejected)
- Search bookmarks by title
- Filter bookmarks by tag
- SQLite database, so data survives restarts
- Automated tests with pytest

## Requirements

- Python 3.9 or higher

## Setup

```bash
git clone <your-repo-url>
cd bookmarks-api
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Run the API

```bash
fastapi dev app/main.py
```

Open http://127.0.0.1:8000/docs for the interactive documentation.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/bookmarks` | Create a bookmark |
| GET | `/bookmarks` | List bookmarks (optional `search` and `tag`) |
| GET | `/bookmarks/{id}` | Get one bookmark |
| PUT | `/bookmarks/{id}` | Replace a bookmark |
| DELETE | `/bookmarks/{id}` | Delete a bookmark |

## Example

Create a bookmark:

```json
{
  "title": "Python",
  "url": "https://python.org",
  "tags": ["coding"]
}
```

Search and filter:

```
GET /bookmarks?search=python
GET /bookmarks?tag=coding
```

## Run the tests

```bash
python -m pytest
```

## Project structure

```
app/
  main.py        API endpoints
  schemas.py     Pydantic models
  models.py      SQLAlchemy table
  database.py    Database connection
tests/
  conftest.py    Test database fixture
  test_api.py    Tests
```