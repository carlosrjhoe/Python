from .models import Todo
from .serializers import TodoSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST']) # Função decorator com argumentos (GET e POST)
def todo_list(request):
    if request.method == 'GET': # Pegar todos os objetos
        todo = Todo.objects.all() 
        serializer = TodoSerializers(todo, many=True) # Class de serializer
        return Response(serializer.data) # Response
    elif request.method == 'POST': # Pegar adicionar novos objetos
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid(): # Verificar objeto está correto
            serializer.save() # Salvar objeto
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)