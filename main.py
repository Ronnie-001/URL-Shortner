from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> str:
    return "A URL Shortner!"


@app.get("/api/v1/urls/shorten")
async def shortenURL():
    print()

@app.get("/api/v1/urls/{url_id}")
async def getURL():
    print()


