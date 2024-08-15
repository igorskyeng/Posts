from rest_framework import serializers


class IndividualEntrepreneurValidator:
    """
    Класс для запрета выбора двух поставщиков.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        supplier_factory = value.get(self.field)
        supplier_retail_network = value.get('supplier_retail_network')

        if supplier_factory and supplier_retail_network:
            raise serializers.ValidationError('Нельзя выбрать два поставщика.')
