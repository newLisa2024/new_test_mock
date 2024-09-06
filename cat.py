import requests

def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)

    if response.status_code == 200:
        # Ответ приходит в виде списка, берем первый элемент
        cat_image = response.json()[0]['url']
        return cat_image
    else:
        return None


# Пример использования
random_cat_image_url = get_random_cat_image()
if random_cat_image_url:
    print(f"Вот случайное изображение кошки: {random_cat_image_url}")
else:
    print("Не удалось получить изображение кошки.")
