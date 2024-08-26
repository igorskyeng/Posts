from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from main.models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Класс для вывода в админ панель атрибутов модели 'Пост'.
    """
    list_display = ('id', 'title', 'text', 'image', 'autor', 'date_of_creation', 'date_of_editing')
    list_filter = ('date_of_creation',)
    search_fields = ('title', 'date_of_creation')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """
    Класс для вывода в админ панель атрибутов модели 'Комментарии'.
    """
    list_display = ('id', 'post', 'autors', 'text', 'date_of_creation', 'date_of_editing')
    list_filter = ('date_of_creation',)
    search_fields = ('autors', 'date_of_creation')

    def autors(self, obj):
        """
        Функция для вывода интерактивной ссылки в атрибут 'Автор' на привязанную внешним ключом модель.
        :param obj: Получает атрибут 'Автор' из модели 'Пост'.
        :return: Возвращает интерактивную ссылку на модель.
        """
        link = reverse("admin:main_post_change", args=[obj.autor.id])
        return format_html('<a href="{}">{}</a>', link, obj.autor)
