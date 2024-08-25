from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель "Пользователь".
    """
    email = models.EmailField(unique=True, verbose_name='Почта')
    password = models.CharField(max_length=150, verbose_name='Пароль', **NULLABLE)
    phone = models.CharField(max_length=150, verbose_name='Телефон', **NULLABLE)
    date_of_birth = models.DateTimeField(verbose_name='Дата рождения', default=datetime.now())
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', default=datetime.now())
    date_of_editing = models.DateTimeField(verbose_name='Дата редактирования', **NULLABLE)
    token = models.CharField(max_length=24, verbose_name='Токен верификации', **NULLABLE)

    USERNAME_FIELD = "email"
    username = USERNAME_FIELD
    REQUIRED_FIELDS = []
