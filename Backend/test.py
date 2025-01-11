import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_new_chat(client):
    response = client.post('/new_chat', data={'file': (open('chat1.txt', 'rb'), 'chat1.txt')})
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'chat_id' in json_data

def test_chat(client):
    response = client.post('/chat/chat1', json={'prompt': 'Hello, bot!'})
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'conversation' in json_data

def test_conversation(client):
    response = client.get('/conversation/chat1')
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'conversation' in json_data

def test_reset_chat(client):
    response = client.delete('/reset_chat/chat1')
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'message' in json_data
