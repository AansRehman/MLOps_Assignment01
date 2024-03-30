# import pytest
# from app import app

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_predict(client):
#     json_data = {
#         "Pregnancies": 2,
#         "Glucose": 91,
#         "BloodPressure": 62,
#         "SkinThickness": 0,
#         "Insulin": 0,
#         "BMI": 27.3,
#         "DiabetesPedigreeFunction": 0.525,
#         "Age": 22
#     }
#     response = client.post('/predict', json=json_data)
#     assert response.status_code == 200
#     assert response.json['prediction'] == 'Negative'
#     print(response)

import unittest

def add(x, y):
    """Function to add two numbers"""
    return x + y

class TestAddFunction(unittest.TestCase):
    """Test case for the add function"""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers"""
        result = add(2, -3)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
