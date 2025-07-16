from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root() -> str:
    return "A URL Shortner!"

@router.get("/api/v1/urls/shorten")
async def shortenURL():
    print()

@router.get("/api/v1/urls/{url_id}")
async def getURL():
    print()
