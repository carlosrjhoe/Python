from django.urls import path
from . import views
from app.views import todo_list, todo_detail_change_and_delete

app_name = 'app'

urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', todo_detail_change_and_delete),
]
