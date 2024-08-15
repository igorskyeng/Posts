from rest_framework import serializers
from main.models import Factory, RetailNetwork, IndividualEntrepreneur
from main.validators import IndividualEntrepreneurValidator


class FactorySerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Завод'.
    """
    class Meta:
        model = Factory
        fields = '__all__'


class FactoryUpdateSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Завод'
    без возможности изменить поле 'Задолжность'..
    """
    class Meta:
        model = Factory
        exclude = ['debt']


class RetailNetworkSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Розничная сеть'.
    """
    class Meta:
        model = RetailNetwork
        fields = '__all__'


class RetailNetworkUpdateSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Розничная сеть'
    без возможности изменить поле 'Задолжность'..
    """
    class Meta:
        model = RetailNetwork
        exclude = ['debt']


class IndividualEntrepreneurSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Индивидуальный предприниматель'.
    """
    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        validators = [IndividualEntrepreneurValidator(field='supplier_factory')]


class IndividualEntrepreneurUpdateSerializers(serializers.ModelSerializer):
    """
    Сериалайзер для вывода всех атрибутов модели 'Индивидуальный предприниматель'
    без возможности изменить поле 'Задолжность'.
    """
    class Meta:
        model = IndividualEntrepreneur
        exclude = ['debt']
        validators = [IndividualEntrepreneurValidator(field='supplier_factory')]