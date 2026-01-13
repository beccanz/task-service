# Event-Driven Task Service

A backend service built with FastAPI and async SQLAlchemy that manages tasks and their lifecycle.

This project is a personal learning exercise focused on:
- Clean API design
- Validation and correctness
- Async Python backend patterns
- Testable, production-style structure

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy (async)
- SQLite (local dev)
- Pytest
- Docker & docker-compose

---

## Features

- Create, fetch, list, and update tasks
- Input validation with Pydantic
- Proper HTTP status codes
- Async database access
- Swagger UI for exploration
- Automated tests

---

## Running Locally (Docker)

```bash
docker compose up --build
