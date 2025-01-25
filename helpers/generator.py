from faker import Faker

faker_ru = Faker('ru_RU')


def generate_user_data():
    return {
        "name": faker_ru.first_name(),
        "surname": faker_ru.last_name(),
        "phone": faker_ru.numerify(text="+79#########"),
        "comment": faker_ru.sentence()
    }
