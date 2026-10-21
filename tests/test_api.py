def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}



def test_create_bookmark(client):
    response = client.post(
        "/bookmarks",
        json={"title": "Python", "url": "https://python.org", "tags": ["coding"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Python"
    assert data["tags"] == ["coding"]



def test_get_missing_bookmark_returns_404(client):
    response = client.get("/bookmarks/999")
    assert response.status_code == 404
