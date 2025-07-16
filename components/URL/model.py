from sqlalchemy import Date, String, True_
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.orm import Mapped

class Base(DeclarativeBase): 
    pass

class User(Base):
    __tablename__ = "urls"

    uid: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str] = mapped_column(String(100)) 
    long_url: Mapped[str] = mapped_column(String(100)) 
    created_at: Mapped[Date] 
    use_count: Mapped[int] 
