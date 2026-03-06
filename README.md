# Task Manager API

A simple REST API for managing tasks built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

This project demonstrates how to build a backend API with common features such as CRUD operations, filtering, pagination, and search.

This project was created as a learning exercise to practice building REST APIs using FastAPI and SQLAlchemy.

---

## Features

The API supports the following functionality:

- Create tasks
- Get a list of tasks
- Get a single task by ID
- Update task title
- Mark task as completed
- Delete tasks
- Filter tasks by completion status
- Search tasks by title
- Pagination (limit and offset)

Each task contains:

- id
- title
- description
- completed status
- created_at timestamp

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

---

## Requirements

Python 3.10+

---

## Project Structure

```text
app/
├── main.py        # FastAPI application and routes
├── models.py      # SQLAlchemy models
├── schemas.py     # Pydantic schemas
├── crud.py        # Database operations
├── database.py    # Database connection
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
```

Create and activate a virtual environment.

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Linux / Mac:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Server

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Example Requests

Create a task:

```
POST /tasks
```

Example request body:

```json
{
  "title": "Learn FastAPI",
  "description": "Build a task manager API"
}
```

Get all tasks:

```
GET /tasks
```

Filter completed tasks:

```
GET /tasks?completed=true
```

Search tasks:

```
GET /tasks?search=python
```

Pagination:

```
GET /tasks?limit=10&offset=10
```

Mark task as completed:

```
PUT /tasks/{task_id}/complete
```

Delete task:

```
DELETE /tasks/{task_id}
```

---

## License

This project is open-source and intended for educational purposes.