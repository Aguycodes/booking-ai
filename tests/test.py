import requests

BASE_URL = "http://127.0.0.1:8000"

def test_analytics():
    response = requests.post(f"{BASE_URL}/analytics")
    assert response.status_code == 200
def test_ask():
    response = requests.post(f"{BASE_URL}/ask", json={"question": "Show me the total revenue for July 2017"})
    assert response.status_code == 200
    assert "result" in response.json()