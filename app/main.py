from fastapi import FastAPI

app = FastAPI(title="Bookmarks API")


@app.get("/")
def read_root():
    return {"message": "Bookmarks API is running"}


@app.get ("/health")
def health_check():
    return {"status":"ok"} 