from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import QuerySet
from main.models import Factory, RetailNetwork, IndividualEntrepreneur


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """
    Класс для вывода в админ панель атрибутов модели 'Забод'.
    """
    actions = ['admin_action']
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                    'market_launch_date', 'debt', 'time_of_creation')
    list_filter = ('city',)
    search_fields = ('name', 'name_product')

    @admin.action(description="Очистить задолженность перед поставщиком")
    def admin_action(self, request, qs: QuerySet):
        """
        функция для очистки атрибута модели 'Задолжность перед поставщиком.'
        """
        qs.update(debt=0)


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    """
    Класс для вывода в админ панель атрибутов модели 'Розничная сеть'.
    """
    actions = ['admin_action']
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                    'market_launch_date', 'suppliers', 'debt', 'time_of_creation')
    list_filter = ('city',)
    search_fields = ('name', 'name_product')

    def suppliers(self, obj):
        """
        Функция для вывода интерактивной ссылки в атрибут 'Поставщики' на привязанную внешним ключом модель.
        :param obj: Получает атрибут 'Поставщики' из модели 'Розничная сеть'.
        :return: Возвращает интерактивную ссылку на модель.
        """
        link = reverse("admin:main_factory_change", args=[obj.supplier_retail_network.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier_retail_network)

        suppliers.short_description = "supplier_retail_network"

    @admin.action(description="Очистить задолженность перед поставщиком")
    def admin_action(self, request, qs: QuerySet):
        """
        функция для очистки атрибута модели 'Задолжность перед поставщиком'.
        """
        qs.update(debt=0)


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    """
    Класс для вывода в админ панель атрибутов модели 'Индивидуальный предприниматель'.
    """
    actions = ['admin_action']
    list_display = ('name_IE', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                    'market_launch_date', 'suppliers', 'debt', 'time_of_creation')
    list_filter = ('city',)
    search_fields = ('name_IE', 'name_product')

    def suppliers(self, obj):
        """
        Функция для вывода интерактивной ссылки в атрибут 'Поставщики' на привязанную внешним ключом модель.
        :param obj: Получает атрибут 'Поставщики' из модели 'Индивидуальный предприниматель'.
        :return: Возвращает интерактивную ссылку на модель.
        """
        if obj.supplier_factory:
            link = reverse("admin:main_factory_change", args=[obj.supplier_factory.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier_factory)

        else:
            link = reverse("admin:main_retailnetwork_change", args=[obj.supplier_retail_network.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier_retail_network)

        suppliers.short_description = "supplier_retail_network"

    @admin.action(description="Очистить задолженность перед поставщиком")
    def admin_action(self, request, qs: QuerySet):
        """
        функция для очистки атрибута модели 'Задолжность перед поставщиком.'
        """
        qs.update(debt=0)
