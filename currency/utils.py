import requests


def get_currency_data():
    try:
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        print(e)
        return []
