import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.api.router import api_router
from app.seed import seed_demo_inventory

logger = logging.getLogger("smartcart")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting SmartCart server...")
    settings = get_settings()
    logger.info(f"LLM Provider: {settings.llm_provider} | Model: {settings.llm_model}")
    logger.info(f"Embedding Provider: {settings.embedding_provider} | Model: {settings.embedding_model}")

    seed_demo_inventory()
    logger.info("Demo inventory seeded.")

    yield
    logger.info("Shutting down SmartCart server.")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="SmartCart API",
        description="RAG-based Virtual Shopping Assistant",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    return app


app = create_app()
