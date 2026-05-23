import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client):
    response = client.get('/')
    assert response.status_code in [200, 404]

def test_create_task_no_data(client):
    response = client.post('/tasks')
    assert response.status_code == 400
