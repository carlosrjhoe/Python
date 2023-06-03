from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .serializers import TodoSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# def index(request):
#     return render(request, 'app/index.html')

@api_view(['GET'])
def todo_list(request):
    todo = Todo.objects.all()
    serializer = TodoSerializers(todo, many=True)
    return Response(serializer.data)