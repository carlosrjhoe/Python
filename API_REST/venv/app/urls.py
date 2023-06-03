from django.urls import path
from . import views
from app.views import todo_list

app_name = 'app'

urlpatterns = [
    path('', todo_list),
]
