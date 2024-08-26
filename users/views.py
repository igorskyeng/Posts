from datetime import datetime
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.permissions import Admin, IsOwner
from users.serliazers import UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    """
    Создание пользователя.
    """
    serializer_class = UserSerializers
    permission_classes = [AllowAny]

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
    permission_classes = [IsAuthenticated | Admin]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр пользователя.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated | Admin]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление пользователя.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [Admin | IsOwner]

    def perform_update(self, serializer):
        new_user = serializer.save()
        new_user.date_of_editing = datetime.now()
        new_user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [Admin]
