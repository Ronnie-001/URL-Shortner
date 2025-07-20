from sqlalchemy import Column, Date, Integer, String, true 
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from components.database.dbconn import Base 

from datetime import datetime

class URL(Base):
    __tablename__ = "urls"
    
    uid = Column(Integer, primary_key=True, autoincrement=True)
    short_url = Column(String(100))
    long_url = Column(String(100))
    created_at = Column(Date)
    use_count = Column(Integer)
    
    def __repr__(self) -> str:
        return f"ID(uid={self.uid!r}), short_url={self.short_url!r}, long_url={self.long_url!r}, created_at={self.created_at!r}, use_count={self.use_count!r}"

