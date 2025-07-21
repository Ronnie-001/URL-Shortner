# pydantic models used to specify what users must enter
from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    long_url: HttpUrl

class URLUpdate(BaseModel):
    short_url: str | None = None
    long_url: str | None = None
    use_count: int | None = None

    class Config:
        from_attributes = True
