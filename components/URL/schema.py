# pydantic models used to specify what users must enter
from datetime import datetime
from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    long_url: HttpUrl

class URLRead(BaseModel):
    uid: int
    short_url: str
    long_url: str
    cretaed_at: datetime
    use_count: int

    class Config:
        from_attributes = True
