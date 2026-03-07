import pytest
from app import app, init_db
import os

@pytest.fixture
def client():
    # Setup: Initialize a temporary database for testing
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'test_aceest.db'
    
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client
    
    # Teardown: Remove the test database after tests finish
    if os.path.exists('aceest_fitness.db'):
        os.remove('aceest_fitness.db')

def test_home_page(client):
    """Validates the Flask application functions as specified[cite: 37]."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEest Functional Fitness" in response.data

def test_calculation_and_storage(client):
    """Validates internal logic and database persistence."""
    test_data = {
        "name": "DevOps User",
        "weight": 80,
        "program": "Fat Loss (FL)"
    }
    # Fat Loss factor is 22. 80 * 22 = 1760
    response = client.post('/calculate', json=test_data)
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['calories'] == 1760
    assert "Saved" in data['status']

def test_client_listing(client):
    """Tests the retrieval of stored client data."""
    # First, save a client
    client.post('/calculate', json={
        "name": "Test Client", "weight": 70, "program": "Beginner (BG)"
    })
    
    # Then, check the list endpoint
    response = client.get('/clients')
    data = response.get_json()
    
    assert response.status_code == 200
    assert any(c['name'] == "Test Client" for c in data)