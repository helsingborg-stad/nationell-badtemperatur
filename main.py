import uvicorn
from fastapi import FastAPI, APIRouter

from api.health_check import check_router
from api.iot import iot_router


def create_fast_api_app() -> FastAPI:
    app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})

    api = APIRouter(prefix="/api")
    api.include_router(check_router)
    api.include_router(iot_router)

    app.include_router(api)

    return app


app_instance = create_fast_api_app()

if __name__ == "__main__":
    uvicorn.run('main:app_instance', reload=True)
