from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name = "home"),
    path('profilo/<username>', views.profilo, name = "show_profilo"),
    path('users-list', views.UtentiListView.as_view(), name = "show_utenti"),
    path('cerca/', views.cerca, name = "f_cerca"),
]
