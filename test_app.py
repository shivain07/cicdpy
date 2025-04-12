from app import app

def test_root_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Continuous Delivery Demo!" in response.data
