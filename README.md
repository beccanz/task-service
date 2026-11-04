# Event-Driven Task Service

A production-style task management API demonstrating clean architecture, async PostgreSQL patterns, and comprehensive testing — built to explore modern Python backend practices.

## Key Features

- **Async PostgreSQL** with SQLAlchemy for high-performance database operations
- **RESTful API design** with FastAPI and automatic OpenAPI documentation
- **Input validation** using Pydantic schemas with proper error handling
- **Docker containerization** with docker-compose for reproducible environments
- **Database migrations** ready with Alembic
- **Test coverage** with pytest and async test patterns
- **Production patterns**: connection pooling, health checks, proper logging

---

## Tech Stack

- **Backend:** Python 3.11, FastAPI, SQLAlchemy (async)
- **Database:** PostgreSQL 15 (asyncpg driver)
- **Testing:** Pytest, pytest-asyncio, httpx
- **Infrastructure:** Docker, docker-compose
- **Monitoring:** Prometheus-ready metrics instrumentation

---

## Running Locally (Docker)

### Prerequisites
- Docker & Docker Compose installed

### Quick Start

```bash
# Start PostgreSQL and API service
docker compose up --build
