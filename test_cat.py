import unittest
from unittest.mock import patch
from cat import get_random_cat_image  # Импортируем функцию из cat.py
class TestGetRandomCatImage(unittest.TestCase):

    @patch('cat.requests.get')  # Мокаем метод requests.get в модуле cat
    def test_get_random_cat_image_success(self, mock_get):
        # Данные, которые вернет мок при запросе к API
        mock_response = [
            {
                "id": "abc123",
                "url": "https://cdn2.thecatapi.com/images/abc123.jpg"
            }
        ]
        # Настраиваем mock на возврат объекта с методом .json(), который возвращает mock_response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Вызываем тестируемую функцию
        result = get_random_cat_image()

        # Проверяем, что вернулся правильный URL
        self.assertEqual(result, "https://cdn2.thecatapi.com/images/abc123.jpg")
        # Проверяем, что запрос был сделан один раз
        mock_get.assert_called_once_with('https://api.thecatapi.com/v1/images/search')

    @patch('cat.requests.get')  # Мокаем метод requests.get для неуспешного запроса
    def test_get_random_cat_image_failure(self, mock_get):
        # Настраиваем mock на возврат 404 статуса
        mock_get.return_value.status_code = 404

        # Вызываем тестируемую функцию
        result = get_random_cat_image()

        # Проверяем, что функция возвращает None при неуспешном запросе
        self.assertIsNone(result)
        # Проверяем, что запрос был сделан один раз
        mock_get.assert_called_once_with('https://api.thecatapi.com/v1/images/search')


if __name__ == '__main__':
    unittest.main()

