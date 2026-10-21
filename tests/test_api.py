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


def test_update_bookmark(client):
    client.post(
        "/bookmarks",
        json={"title": "Python", "url": "https://python.org", "tags": ["coding"]},
    )
    response = client.put(
        "/bookmarks/1",
        json={"title": "Python Docs", "url": "https://docs.python.org", "tags": []},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Python Docs"
    assert response.json()["id"] == 1




def test_delete_bookmark(client):
    client.post(
        "/bookmarks",
        json={"title": "Python", "url": "https://python.org", "tags": []},
    )
    response = client.delete("/bookmarks/1")
    assert response.status_code == 204
    assert client.get("/bookmarks/1").status_code == 404


def test_search_by_title(client):
    client.post(
        "/bookmarks",
        json={"title": "Python Tutorial", "url": "https://python.org", "tags": []}
    )
    client.post(
        "/bookmarks",
        json={"title": "Cooking Basics", "url": "https://example.com", "tags": []}
    )
    response = client.get("/bookmarks", params={"search": "python"})
    assert response.status_code == 200
    titles = [b["title"] for b in response.json()]
    assert titles == ["Python Tutorial"]


def test_filter_by_tag(client):
    client.post(
        "/bookmarks",
        json={"title": "Python", "url": "https://python.org", "tags": ["coding"]},
    )
    client.post(
        "/bookmarks",
        json={"title": "Cooking", "url": "https://example.com", "tags": ["food"]},
    )
    response = client.get("/bookmarks", params={"tag": "food"})
    assert response.status_code == 200
    titles = [b["title"] for b in response.json()]
    assert titles == ["Cooking"]


def test_search_no_match_returns_empty_list(client):
    response = client.get("/bookmarks", params={"search": "zzz"})
    assert response.status_code == 200
    assert response.json() == []

