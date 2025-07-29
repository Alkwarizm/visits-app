from main import redis_client


def test_read_root_increments_visits(session, client):

    # Reset visits count before the test
    redis_client.set("visits", 0)

    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "visits" in data
    assert data["visits"] == 1

    # Call again to check if visits increment
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "visits" in data
    assert data["visits"] == 2