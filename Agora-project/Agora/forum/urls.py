from django.urls import path
from . import views

urlpatterns = [
    path("crea-sezione", views.CreaSezione.as_view(), name="creasezione"),
    path("show-sezione/<int:pk>", views.show_sezione, name="show_sezione"),
    path("show-sezione/<int:pk>/crea-discussione", views.crea_discussione, name="crea_discussione"),
    path("discussione/<int:pk>", views.show_discussione, name="show_discussione"),
    path("discussione/<int:pk>/aggiungi-risposta", views.aggiungi_risposta, name="aggiungi_risposta"),
    path("discussione/<int:id>/post/<int:pk>", views.CancellaPost.as_view(), name="elimina_post")

]
