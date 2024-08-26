from rest_framework import serializers
from main.models import Post, Comments
from main.validators import PostValidator


class CommentsSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Комментарии'.
    """
    class Meta:
        model = Comments
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Пост'.
    """
    class Meta:
        model = Post
        fields = '__all__'
        validators = [PostValidator(field='autor')]

    comments = CommentsSerializers(source='comments_set', many=True, read_only=True)


class PostUpdateSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Пост'.
    """
    class Meta:
        model = Post
        fields = '__all__'
