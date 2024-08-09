from django import forms
from main.models import Factory, RetailNetwork, IndividualEntrepreneur


class FactoryAddForm(forms.ModelForm):

    class Meta:
        model = Factory
        fields = ('name', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                  'market_launch_date', 'debt')


class RetailNetworkAddForm(forms.ModelForm):

    class Meta:
        model = RetailNetwork
        fields = ('name', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                  'market_launch_date', 'supplier', 'debt')


class IndividualEntrepreneurAddForm(forms.ModelForm):

    class Meta:
        model = IndividualEntrepreneur
        fields = ('name_IE', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model',
                  'market_launch_date', 'supplier', 'debt')
