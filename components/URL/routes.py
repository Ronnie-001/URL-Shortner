from fastapi import APIRouter
from components.URL.schema import URLCreate, URLRead
import datetime

router = APIRouter()

@router.get("/")
async def root() -> str:
    return "A URL Shortner!"

@router.get("/api/v1/urls/shorten")
async def shortenURL(url: URLCreate):
    currentDate = datetime.date.today()

@router.get("/api/v1/urls/{url_id}")
async def getURL(url: URLRead):
    print()
