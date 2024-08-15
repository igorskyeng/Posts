from django.urls import path

from main.apps import MainConfig
from main.views import FactoryCreateAPIView, FactoryListAPIView, FactoryRetrieveAPIView, FactoryUpdateAPIView, \
    FactoryDestroyAPIView, RetailNetworkCreateAPIView, RetailNetworkListAPIView, RetailNetworkRetrieveAPIView, \
    RetailNetworkUpdateAPIView, RetailNetworkDestroyAPIView, IndividualEntrepreneurCreateAPIView, \
    IndividualEntrepreneurListAPIView, IndividualEntrepreneurRetrieveAPIView, IndividualEntrepreneurUpdateAPIView, \
    IndividualEntrepreneurDestroyAPIView

app_name = MainConfig.name

urlpatterns = [
    path('factory/create/', FactoryCreateAPIView.as_view(), name='factory_create'),
    path('factory/list/', FactoryListAPIView.as_view(), name='factory_list'),
    path('factory/<int:pk>/', FactoryRetrieveAPIView.as_view(), name='factory_get'),
    path('factory/update/<int:pk>/', FactoryUpdateAPIView.as_view(), name='factory_update'),
    path('factory/delete/<int:pk>/', FactoryDestroyAPIView.as_view(), name='factory_delete'),

    path('retail_network/create/', RetailNetworkCreateAPIView.as_view(), name='retail_network_create'),
    path('retail_network/list/', RetailNetworkListAPIView.as_view(), name='retail_network_list'),
    path('retail_network/<int:pk>/', RetailNetworkRetrieveAPIView.as_view(), name='retail_network_get'),
    path('retail_network/update/<int:pk>/', RetailNetworkUpdateAPIView.as_view(), name='retail_network_update'),
    path('retail_network/delete/<int:pk>/', RetailNetworkDestroyAPIView.as_view(), name='retail_network_delete'),

    path('individual_entrepreneur/create/', IndividualEntrepreneurCreateAPIView.as_view(),
         name='individual_entrepreneur_create'),
    path('individual_entrepreneur/list/', IndividualEntrepreneurListAPIView.as_view(),
         name='individual_entrepreneur_list'),
    path('individual_entrepreneur/<int:pk>/', IndividualEntrepreneurRetrieveAPIView.as_view(),
         name='factory_get'),
    path('individual_entrepreneur/update/<int:pk>/', IndividualEntrepreneurUpdateAPIView.as_view(),
         name='individual_entrepreneur_update'),
    path('individual_entrepreneur/delete/<int:pk>/', IndividualEntrepreneurDestroyAPIView.as_view(),
         name='individual_entrepreneur_delete'),
]
