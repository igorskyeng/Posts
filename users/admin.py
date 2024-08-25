from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс для вывода в админ панель атрибутов модели 'Пользователь'.
    """
    list_display = ('id', 'email', 'password', 'phone', 'date_of_birth', 'date_of_creation', 'date_of_editing', 'token')
