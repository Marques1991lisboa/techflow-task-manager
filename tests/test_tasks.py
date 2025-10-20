from src.main import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Nova Tarefa'})
    assert response.status_code == 201

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
