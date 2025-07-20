from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from components.URL.schema import URLCreate
from components.database.dbconn import Session
import components.URL.model as model

import datetime

router = APIRouter()

global_counter = 0

async def getDb():
    async with Session() as session:
        yield session

async def generateShortUrl() -> str:
    global global_counter
    
    num = global_counter
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base = len(characters)
    encoded = ""

    while num > 0:
        num, rem = divmod(num, base)
        encoded = characters[rem] + encoded
    return encoded or characters[0]

@router.post("/api/v1/urls/shorten")
async def shortenURL(url: URLCreate, db: AsyncSession = Depends(getDb)):
    global global_counter

    new_url = model.URL(
        short_url=generateShortUrl(),
        long_url=url.long_url,
        created_at=datetime.datetime.now(),
        use_count = 0
    )

    db.add(new_url)
    await db.commit()
    await db.refresh(new_url)

    global_counter += 1

    return new_url


@router.get("/api/v1/urls/{url_id}")
async def getURL(url_id : int, db: AsyncSession = Depends(getDb)):
    res = await db.execute(select(model.URL).where(model.URL.uid == url_id))
    user = res.scalar_one_or_none()


    return user
