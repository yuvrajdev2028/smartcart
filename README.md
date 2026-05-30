# SmartCart

> RAG-based Virtual Shopping Assistant — SaaS Product

SmartCart is a plug-and-play AI shopping assistant that integrates with any e-commerce store. It understands your product inventory through RAG (Retrieval-Augmented Generation) and helps customers find exactly what they need.

## Architecture

- **Backend** (`server/`) — Python FastAPI with LangChain, ChromaDB, and configurable LLM providers
- **Frontend** (`web/`) — React + ShadCN demo portal with mock store and embedded chatbot

## Quick Start

### Backend

```bash
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your LLM API key
uvicorn app.main:app --reload
```

### Frontend

```bash
cd web
npm install
npm run dev
```

The backend runs on `http://localhost:8000` and the frontend on `http://localhost:5173`.

## Configuration

All settings are controlled via `server/.env`:

| Variable | Default | Description |
|---|---|---|
| `LLM_PROVIDER` | `gemini` | LLM provider: `openai` or `gemini` |
| `LLM_MODEL` | `gemini-2.0-flash` | Model name |
| `LLM_API_KEY` | — | Your API key |
| `EMBEDDING_PROVIDER` | `local` | Embedding: `local`, `openai`, or `gemini` |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Embedding model name |
| `CHROMA_PERSIST_DIR` | `./chroma_data` | ChromaDB storage path |
| `CORS_ORIGINS` | `["http://localhost:5173"]` | Allowed CORS origins |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/chat` | Send a user message, get AI response |
| `POST` | `/api/v1/inventory/sync` | Bulk upsert products |
| `DELETE` | `/api/v1/inventory/{tenant_id}/{product_id}` | Delete a product |
| `GET` | `/api/v1/inventory/{tenant_id}/status` | Check inventory count |
| `GET` | `/api/v1/health` | Health check |
