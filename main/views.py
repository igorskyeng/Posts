from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from main.models import Factory, RetailNetwork, IndividualEntrepreneur
from django_filters import rest_framework as rest_filters
from main.paginators import Paginator
from main.permissions import ActiveUser, IsOwner
from main.serliazers import (FactorySerializers, FactoryUpdateSerializers, RetailNetworkSerializers,
                             RetailNetworkUpdateSerializers, IndividualEntrepreneurSerializers,
                             IndividualEntrepreneurUpdateSerializers)


class FactoryCreateAPIView(generics.CreateAPIView):
    """
    Создание 'Завода'.
    """
    serializer_class = FactorySerializers
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_factory = serializer.save()
        new_factory.user = self.request.user
        new_factory.save()


class FactoryListAPIView(generics.ListAPIView):
    """
    Вывод листа заводов.
    """
    serializer_class = FactorySerializers
    permission_classes = [IsAuthenticated & ActiveUser]
    pagination_class = Paginator
    queryset = Factory.objects.all()

    # Фильтр по определенной стране.
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['country']


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """
    Вывод конкретного завода.
    """
    serializer_class = FactorySerializers
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser]


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление конкретного завода.
    """
    serializer_class = FactoryUpdateSerializers
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser & IsOwner]

    def perform_update(self, serializer):
        new_factory = serializer.save()
        new_factory.save()


class FactoryDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление конкретного завода.
    """
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser & IsOwner]

    def perform_destroy(self, instance):
        instance.delete()


class RetailNetworkCreateAPIView(generics.CreateAPIView):
    """
    Создание 'Розничной сети'.
    """
    serializer_class = RetailNetworkSerializers
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_retail_network = serializer.save()
        new_retail_network.user = self.request.user
        new_retail_network.save()


class RetailNetworkListAPIView(generics.ListAPIView):
    """
    Вывод листа розничныйх сетей.
    """
    serializer_class = RetailNetworkSerializers
    permission_classes = [IsAuthenticated & ActiveUser]
    queryset = RetailNetwork.objects.all()
    pagination_class = Paginator

    # Фильтр по определенной стране.
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['country']


class RetailNetworkRetrieveAPIView(generics.RetrieveAPIView):
    """
    Вывод конкретной розничной сети.
    """
    serializer_class = RetailNetworkSerializers
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser]


class RetailNetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление конкретной розничной сети.
    """
    serializer_class = RetailNetworkUpdateSerializers
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser & IsOwner]

    def perform_update(self, serializer):
        new_retail_network = serializer.save()
        new_retail_network.save()


class RetailNetworkDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление конкретной розничной сети.
    """
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser & IsOwner]

    def perform_destroy(self, instance):
        instance.delete()


class IndividualEntrepreneurCreateAPIView(generics.CreateAPIView):
    """
    Создание 'Индивилдеального предпринимателя'.
    """
    serializer_class = IndividualEntrepreneurSerializers
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_individual_entrepreneur = serializer.save()
        new_individual_entrepreneur.user = self.request.user
        new_individual_entrepreneur.save()


class IndividualEntrepreneurListAPIView(generics.ListAPIView):
    """
    Вывод листа индивилдеальный предпринимателей.
    """
    serializer_class = IndividualEntrepreneurSerializers
    permission_classes = [IsAuthenticated & ActiveUser]
    queryset = IndividualEntrepreneur.objects.all()
    pagination_class = Paginator

    # Фильтр по определенной стране.
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['country']


class IndividualEntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    """
    Вывод конкретного индивилдеального предпринимателя.
    """
    serializer_class = IndividualEntrepreneurSerializers
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser]


class IndividualEntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление конкретного индивилдеального предпринимателя.
    """
    serializer_class = IndividualEntrepreneurUpdateSerializers
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser & IsOwner]

    def perform_update(self, serializer):
        new_individual_entrepreneur = serializer.save()
        new_individual_entrepreneur.save()


class IndividualEntrepreneurDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление конкретного индивилдеального предпринимателя.
    """
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated & ActiveUser & IsOwner]

    def perform_destroy(self, instance):
        instance.delete()
