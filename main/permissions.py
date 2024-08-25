from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Класс проверят является ли пользователь владельцем или суперпользователем.
    """
    def has_object_permission(self, request, view, obj):
        if obj.autor == request.user or request.user.is_superuser:
            return True

        return False


class Admin(BasePermission):
    """
    Класс проверят является ли пользователь администратором.
    """
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Admin').exists() or request.user.is_superuser:
            return True

        return False
