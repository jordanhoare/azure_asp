from __future__ import annotations

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router, tags_metadata

log = logging.getLogger("uvicorn")


def create_application():
    application = FastAPI(
        openapi_tags=tags_metadata,
        title="Hello World 🤖",
        description="🚀",
        version="0.0.1",
        contact={
            "name": "Jordan",
            "url": "https://github.com/jordanhoare/",
            "email": "jordanhoare0@gmail.com",
        },
    )
    application.include_router(api_router)
    return application


app = create_application()

origins = [
    "http://domainname.com",  # app service -> link to env.settings
    "https://domainname.com",  # app service -> link to env.settings
    "http://localhost",
    "http://localhost:8080",
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
