import math
from random import randint
from fastapi.testclient import TestClient
import pytest
from application.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"
    
def test_return_square(mocker):
    mocker.patch(
        "application.main.get_square",
        return_value = 25
    )
    result = 50
    response = client.get("/twice/5")
    assert result == response.json()
    assert response.status_code == 200
    
    
def test_square():
    test_number = 4
    test_expected_result = 16
    
    res = client.get(f"/twice/{test_number}")
    
    assert res.status_code == 200
    assert res.json() == test_expected_result
    
list_of_numbers = [randint(1,10) for i in range(0,10)]

@pytest.mark.parametrize('number', list_of_numbers)
def test_return_square_twice(number: int):
    response = client.get(f"/twice/{number}")
    assert response.status_code == 200
    assert response.json() == math.pow(number, 2)*2