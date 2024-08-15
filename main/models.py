from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    """
    Модель 'Завод'.
    """
    name = models.CharField(max_length=100, verbose_name='Название завода')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома')
    name_product = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    market_launch_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок')
    debt = models.DecimalField(decimal_places=3, max_digits=1000,  verbose_name='Задолжность')
    time_of_creation = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользватель', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'
        ordering = ('id',)


class RetailNetwork(models.Model):
    """
    Модель 'Розничная сеть'.
    """
    name = models.CharField(max_length=100, verbose_name='Название розничной сети')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома')
    name_product = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    market_launch_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок')
    supplier_retail_network = models.ForeignKey(Factory, verbose_name='Поставщик', on_delete=models.CASCADE)
    debt = models.DecimalField(decimal_places=3, max_digits=1000, verbose_name='Задолжность')
    time_of_creation = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользватель', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'
        ordering = ('id',)


class IndividualEntrepreneur(models.Model):
    """
    Модель 'Индивидуальный предприниматель'.
    """
    name_IE = models.CharField(max_length=100, verbose_name='Индивидуальный предприниматель')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома')
    name_product = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    market_launch_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок')
    supplier_factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    supplier_retail_network = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE, verbose_name='Поставщик',
                                                **NULLABLE)
    debt = models.DecimalField(decimal_places=3, max_digits=1000,  verbose_name='Задолжность')
    time_of_creation = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользватель', null=True)

    def __str__(self):
        return self.name_IE

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'
        ordering = ('id',)
