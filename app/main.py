from fastapi import FastAPI

from app.schemas import Bookmark, BookmarkCreate

app = FastAPI(title="Bookmarks API")

bookmarks: list[Bookmark] = []
next_id = 1


@app.get("/")
def read_root():
    return {"message": "Bookmarks API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/bookmarks", response_model=Bookmark)
def create_bookmark(data: BookmarkCreate):
    global next_id
    bookmark = Bookmark(id=next_id, **data.model_dump())
    bookmarks.append(bookmark)
    next_id += 1
    return bookmark


@app.get("/bookmarks", response_model=list[Bookmark])
def list_bookmarks():
    return bookmarks