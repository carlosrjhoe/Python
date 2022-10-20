from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # (name='index') -> Serve para adicionar dinamicamente uma url
    path('sobre/', views.sobre, name='sobre'),
]