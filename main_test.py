import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict(client):
    json_data = {
        "Pregnancies": 2,
        "Glucose": 91,
        "BloodPressure": 62,
        "SkinThickness": 0,
        "Insulin": 0,
        "BMI": 27.3,
        "DiabetesPedigreeFunction": 0.525,
        "Age": 22
    }
    response = client.post('/predict', json=json_data)
    assert response.status_code == 200
    assert response.json['prediction'] == 'Negative'\


print ("Hello HI")
