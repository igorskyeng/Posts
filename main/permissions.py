from rest_framework.permissions import BasePermission
from users.models import User

user = User.objects.first()


class IsOwner(BasePermission):
    """
    Класс проверят является ли пользователь владельцем или суперпользователем.
    """
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True

        return False


class ActiveUser(BasePermission):
    """
    Класс проверят активный ли позиватель или является суперпользователем.
    """
    def has_object_permission(self, request, view, obj):
        if user.is_active is True or request.user.is_superuser:
            return True

        return False