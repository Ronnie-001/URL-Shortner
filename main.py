from fastapi import FastAPI
from components.URL.routes import router 

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root() -> str:
    return "URL shortner!"
