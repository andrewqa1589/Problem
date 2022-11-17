import requests

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Создание случайной шутки"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы поулчили новую шутку")
        else:
            print("Провал!!! Запрос ошибочный")
        result.encoding = 'utf-8'
        print(result.text)


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()



