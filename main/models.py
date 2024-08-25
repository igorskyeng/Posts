from datetime import datetime
from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Comments(models.Model):
    """
    Модель 'Коммунтарии'.
    """
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                      verbose_name='Автор Комментария', null=True)
    text = models.TextField(verbose_name='Текст')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', default=datetime.now())
    date_of_editing = models.DateTimeField(verbose_name='Дата редактирования', **NULLABLE)

    def __str__(self):
        return str(self.autor)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('id',)


class Post(models.Model):
    """
    Модель 'Посты'.
    """
    title = models.CharField(max_length=100, verbose_name='Зоголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='main/', verbose_name='Изображение', **NULLABLE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор', null=True)
    comments = models.ForeignKey(Comments, verbose_name='Комментарии', on_delete=models.CASCADE, **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', default=datetime.now())
    date_of_editing = models.DateTimeField(verbose_name='Дата редактирования', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('id',)
