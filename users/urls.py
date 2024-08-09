from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('message_verification/', TemplateView.as_view(template_name='users/message_verification.html'),
         name='message_verification'),
    path('successfully/', TemplateView.as_view(template_name='users/successfully.html'), name='successfully'),
    path('unsuccessfully/', TemplateView.as_view(template_name='users/unsuccessfully.html'), name='unsuccessfully'),
]
