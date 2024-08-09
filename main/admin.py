from django.contrib import admin
from main.models import Factory, RetailNetwork, IndividualEntrepreneur


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                    'market_launch_date', 'debt', 'time_of_creation')
    list_filter = ('name',)
    search_fields = ('name', 'name_product')


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                    'market_launch_date', 'supplier', 'debt', 'time_of_creation')
    list_filter = ('name',)
    search_fields = ('name', 'name_product')


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name_IE', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                    'market_launch_date', 'supplier', 'debt', 'time_of_creation')
    list_filter = ('name_IE',)
    search_fields = ('name_IE', 'name_product')
