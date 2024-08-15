from rest_framework import generics
from users.models import User
from users.serliazers import UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    """
    Создание пользователя.
    """
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """
    Просмотр листа пользователей.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр пользователя.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление пользователя.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()
