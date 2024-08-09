from django.urls import path

from main.apps import MainConfig
from main.views import HomeListView, FactoryListView, FactoryCreateView, FactoryDetailtView, FactoryUpdateView, \
    FactoryDeleteView, RetailNetworkListView, RetailNetworkCreateView, RetailNetworkDetailtView, \
    RetailNetworkUpdateView, RetailNetworkDeleteView, IndividualEntrepreneurListView, IndividualEntrepreneurCreateView, \
    IndividualEntrepreneurDetailtView, IndividualEntrepreneurUpdateView, IndividualEntrepreneurDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_list'),
    path('factory_list/', FactoryListView.as_view(), name='factory_list'),
    path('add_factory/', FactoryCreateView.as_view(), name='create_factory'),
    path('view_factory/<int:pk>/', FactoryDetailtView.as_view(), name='factory_detail'),
    path('edit_factory/<int:pk>', FactoryUpdateView.as_view(), name='factory_edit'),
    path('delete_factory/<int:pk>', FactoryDeleteView.as_view(), name='delete_factory'),

    path('retail_network_list/', RetailNetworkListView.as_view(), name='retail_network_list'),
    path('add_retail_network/', RetailNetworkCreateView.as_view(), name='create_retail_network'),
    path('view_retail_network/<int:pk>/', RetailNetworkDetailtView.as_view(), name='retail_network_detail'),
    path('edit_retail_network/<int:pk>', RetailNetworkUpdateView.as_view(), name='retail_network_edit'),
    path('delete_retail_network/<int:pk>', RetailNetworkDeleteView.as_view(), name='delete_retail_network'),

    path('IE_list/', IndividualEntrepreneurListView.as_view(), name='IE_list'),
    path('add_IE/', IndividualEntrepreneurCreateView.as_view(), name='create_IE'),
    path('view_IE/<int:pk>/', IndividualEntrepreneurDetailtView.as_view(), name='IE_detail'),
    path('edit_IEy/<int:pk>', IndividualEntrepreneurUpdateView.as_view(), name='IE_edit'),
    path('delete_IE/<int:pk>', IndividualEntrepreneurDeleteView.as_view(), name='delete_IE'),
]
