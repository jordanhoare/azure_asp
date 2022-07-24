from fastapi import APIRouter

from app.api.endpoints import helloworld

api_router = APIRouter()

api_router.include_router(helloworld.router, prefix="", tags=["FastAPI"])

tags_metadata = [
    {
        "name": "FastAPI",
        "description": "Hello World",
        # "externalDocs": {
        #     "description": "Repository",
        #     "url": "https://github.com/",
        # },
    },
]
