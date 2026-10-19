from pydantic import BaseModel,HttpUrl



class BookmarkCreate(BaseModel):
    title: str
    url: HttpUrl
    tags: list[str] = []


class Bookmark(BookmarkCreate):
    id: int
