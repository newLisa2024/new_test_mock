import pytest
from main import get_wheather

def test_get_wheather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 300}
    }

    api_key = 'test_api_key'
    city = 'London'

    wheather_data = get_wheather(api_key, city)

    assert wheather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'test_api_key'
    city = 'London'

    wheather_data = get_wheather(api_key, city)

    assert wheather_data is None
