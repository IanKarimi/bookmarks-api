from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session


from app import models
from app.database import Base, SessionLocal, engine
from app.schemas import Bookmark, BookmarkCreate


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Bookmarks API")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def tags_to_text(tags: list[str]) -> str:
    return ",".join(tags)



def to_schema(row: models.BookmarkDB) -> Bookmark:
    return Bookmark(
        id=row.id,
        title=row.title,
        url=row.url,
        tags=row.tags.split(",") if row.tags else [],
    )



@app.get("/")
def read_root():
    return {"message":"Bookmarks API is running"}



@app.get("/health")
def health_check():
    return {"status": "ok"}



@app.post("/bookmarks", response_model=Bookmark)
def create_bookmark(data: BookmarkCreate, db: Session = Depends(get_db)):
    row = models.BookmarkDB(
        title=data.title,
        url=str(data.url),
        tags=tags_to_text(data.tags),
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return to_schema(row)


@app.get("/bookmarks", response_model=list[Bookmark])
def list_bookmarks(db: Session = Depends(get_db)):
    rows = db.scalars(select(models.BookmarkDB)).all()
    return [to_schema(row) for row in rows]


@app.get("/bookmarks/{bookmark_id}", response_model=Bookmark)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    row = db.get(models.BookmarkDB, bookmark_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return to_schema(row)




@app.put("/bookmarks/{bookmark_id}", response_model=Bookmark)
def update_bookmark(
    bookmark_id: int, data: BookmarkCreate, db: Session = Depends(get_db)
):

    row = db.get(models.BookmarkDB, bookmark_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    row.title = data.title
    row.url = str(data.url)
    row.tags = tags_to_text(data.tags)
    db.commit()
    db.refresh(row)
    return to_schema(row)



@app.delete("/bookmarks/{bookmark_id}", status_code=204)
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    row = db.get(models.BookmarkDB, bookmark_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.delete(row)
    db.commit()





