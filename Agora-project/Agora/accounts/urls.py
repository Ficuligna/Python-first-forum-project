from django.urls import path
from . import views

urlpatterns = [
    path('nuovo-account', views.registrazione, name='newaccount'),
]
