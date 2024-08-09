import random

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from pytils.translit import slugify

from main.models import Factory, RetailNetwork, IndividualEntrepreneur
from main.forms import FactoryAddForm, RetailNetworkAddForm, IndividualEntrepreneurAddForm


class HomeListView(ListView):
    model = Factory
    template_name = 'main/home_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['factory'] = Factory.objects.all().count()
        context_data['retail_network'] = RetailNetwork.objects.all().count()
        context_data['IE'] = IndividualEntrepreneur.objects.all().count()
        context_data['title'] = 'Главная'
        return context_data


class FactoryCreateView(LoginRequiredMixin, CreateView):
    model = Factory
    form_class = FactoryAddForm
    success_url = reverse_lazy('main:factory_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Добавление завода'

        return context_data

    def form_valid(self, form):
        factory = form.save()
        factory.user = self.request.user
        factory.save()

        return super().form_valid(form)


class FactoryListView(LoginRequiredMixin, ListView):
    model = Factory
    template_name = "main/factory_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        factory = Factory.objects.all()

        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = factory
        context_data['title'] = 'Заводы'

        return context_data


class FactoryDetailtView(LoginRequiredMixin, DetailView):
    model = Factory

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Просмотр завода'

        return context_data


class FactoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Factory
    form_class = FactoryAddForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Редактирование завода'

        return context_data

    def test_func(self):
        if self.get_object().user == self.request.user or self.request.user.is_superuser:
            return True

        else:
            return self.handle_no_permission()

    def get_success_url(self):
        return reverse('main:factory_detail', args=[self.kwargs.get('pk')])


class FactoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Factory
    success_url = reverse_lazy('main:factory_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Удаление завода'

        return context_data


class RetailNetworkCreateView(LoginRequiredMixin, CreateView):
    model = RetailNetwork
    form_class = RetailNetworkAddForm
    success_url = reverse_lazy('main:retail_network_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Добавление розничной сети'

        return context_data

    def form_valid(self, form):
        retail_network = form.save()
        retail_network.user = self.request.user
        retail_network.save()

        return super().form_valid(form)


class RetailNetworkListView(LoginRequiredMixin, ListView):
    model = RetailNetwork
    template_name = "main/retailnetwork_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        retail_network = RetailNetwork.objects.all()
        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = retail_network
        context_data['title'] = 'Розничные сети'

        return context_data


class RetailNetworkDetailtView(LoginRequiredMixin, DetailView):
    model = RetailNetwork

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Просмотр розничных сетей'

        return context_data


class RetailNetworkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RetailNetwork
    form_class = RetailNetworkAddForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Редактирование розничной сети'

        return context_data

    def test_func(self):
        if self.get_object().user == self.request.user or self.request.user.is_superuser:
            return True

        else:
            return self.handle_no_permission()

    def get_success_url(self):
        return reverse('main:retail_network_detail', args=[self.kwargs.get('pk')])


class RetailNetworkDeleteView(LoginRequiredMixin, DeleteView):
    model = RetailNetwork
    success_url = reverse_lazy('main:retail_network_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Удаление розничной сети'

        return context_data


class IndividualEntrepreneurCreateView(LoginRequiredMixin, CreateView):
    model = IndividualEntrepreneur
    form_class = IndividualEntrepreneurAddForm
    success_url = reverse_lazy('main:IE_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Добавление ИП'

        return context_data

    def form_valid(self, form):
        individual_entrepreneur = form.save()
        individual_entrepreneur.user = self.request.user
        individual_entrepreneur.save()

        return super().form_valid(form)


class IndividualEntrepreneurListView(LoginRequiredMixin, ListView):
    model = IndividualEntrepreneur
    template_name = "main/individualentrepreneur_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        individual_entrepreneur = IndividualEntrepreneur.objects.all()
        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = individual_entrepreneur
        context_data['title'] = 'Все ИП'

        return context_data


class IndividualEntrepreneurDetailtView(LoginRequiredMixin, DetailView):
    model = IndividualEntrepreneur

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Просмотр всех ИП'

        return context_data


class IndividualEntrepreneurUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = IndividualEntrepreneur
    form_class = IndividualEntrepreneurAddForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Редактирование ИП'

        return context_data

    def test_func(self):
        if self.get_object().user == self.request.user or self.request.user.is_superuser:
            return True

        else:
            return self.handle_no_permission()

    def get_success_url(self):
        return reverse('main:IE_detail', args=[self.kwargs.get('pk')])


class IndividualEntrepreneurDeleteView(LoginRequiredMixin, DeleteView):
    model = IndividualEntrepreneur
    success_url = reverse_lazy('main:IE_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Удаление ИП'

        return context_data
