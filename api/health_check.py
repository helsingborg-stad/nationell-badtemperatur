from fastapi import APIRouter

check_router = APIRouter(prefix="/check", tags=["check"])


@check_router.get("/health")
async def message():
    return {"message": "I'm healthy!"}
