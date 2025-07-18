from sqlalchemy import String 
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from database.dbconn import Base 

from datetime import datetime

class URL(Base):
    __tablename__ = "urls"

    uid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    short_url: Mapped[str] = mapped_column(String(100)) 
    long_url: Mapped[str] = mapped_column(String(100)) 
    created_at: Mapped[datetime] 
    use_count: Mapped[int] 

    def __repr__(self) -> str:
        return f"ID(uid={self.uid!r}), short_url={self.short_url!r}, long_url={self.long_url!r}, created_at={self.created_at!r}, use_count={self.use_count!r}"

