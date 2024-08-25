from rest_framework import serializers
from main.models import Post, Comments
from main.validators import PostValidator


class PostSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Пост'.
    """
    class Meta:
        model = Post
        fields = '__all__'
        validators = [PostValidator(field='autor')]


class CommentsSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Комментарии'.
    """
    class Meta:
        model = Comments
        fields = '__all__'
