# Antigravity IDE - Backend

This is the FastAPI backend for the Antigravity IDE, acting as the brain for the Jarvis-style frontend. It utilizes a multi-agent architecture (LangGraph) and advanced RAG optimized for structured documents.

## Tech Stack
- **Framework:** FastAPI
- **Agent Orchestration:** LangGraph
- **LLM Gateway:** LiteLLM
- **Database (Relational):** PostgreSQL + SQLAlchemy 2.0 (asyncio) + Alembic
- **Database (Vector):** Qdrant
- **Async Task Queue:** Celery + Redis

## Getting Started

1. Ensure `uv` is installed.
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
3. Run the development server:
   ```bash
   uvicorn src.main:app --reload
   ```
