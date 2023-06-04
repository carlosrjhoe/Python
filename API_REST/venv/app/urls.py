from django.urls import path
from . import views
from app.views import TodoListAndCreate, TodoDetailChangeAndDelete

app_name = 'app'

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]
