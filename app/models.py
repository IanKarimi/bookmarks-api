from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base



class BookmarkDB(Base):
    __tablename__= "bookmarks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    url: Mapped[str] = mapped_column(String(2048))
    tags: Mapped[str] = mapped_column(String(500), default="")
