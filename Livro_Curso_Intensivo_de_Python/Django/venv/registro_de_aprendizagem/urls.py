from django.urls import path
from . import views

app_name = 'registro_de_aprendizagem'

urlpatterns = [
    path('', views.ListaRegistro.as_view(), name="lista"),
]