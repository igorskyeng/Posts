from rest_framework import serializers
from users.models import User
from datetime import date


class UserValidator:
    """
    Класс для проверки домена, количества символов в пароле т содержит ли он цифры.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        password = value.get(self.field)
        email = value.get('email')
        number = any(character.isdigit() for character in password)

        if len(password) < 8:
            raise serializers.ValidationError('Пароль должен содержать не менее 8 символов.')

        print(number)
        if number is False:
            raise serializers.ValidationError('В пароле должны присутствовать цифры')

        if 'mail.ru' not in email and 'yandex.ru' not in email:
            raise serializers.ValidationError('Разрешается использовать только домены: mail.ru, yandex.ru')
