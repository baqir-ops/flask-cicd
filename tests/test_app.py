from app import app


def test_home_status():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_home_content():
    client = app.test_client()
    response = client.get('/')
    data = response.get_json()
    assert data['author'] == 'baqir-ops'


def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200


def test_health_content():
    client = app.test_client()
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'healthy'
