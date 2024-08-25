from rest_framework import serializers
from datetime import date


class PostValidator:
    """
    Класс для запрета введения запрещенных слов и проверка возроста автора.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        autor = value.get(self.field)
        title = value.get('title')
        today = date.today()
        print(autor.date_of_birth)
        age = today.year - autor.date_of_birth.year
        list_words = ['ерунда', 'глупость', 'чепуха']

        if age < 18:
            raise serializers.ValidationError('Автору поста меньше 18 лет.')

        for word in list_words:
            if word in title:
                raise serializers.ValidationError('В заголовке содержится запрещенное слово.')
