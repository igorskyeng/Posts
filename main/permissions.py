from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Класс проверят является ли пользователь владельцем или суперпользователем.
    """
    def has_object_permission(self, request, view, obj):
        if obj.autor == request.user or request.user.is_superuser:
            return True

        return False
