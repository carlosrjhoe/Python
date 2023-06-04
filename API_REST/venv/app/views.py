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
        serializer = TodoSerializers(data=request.data) # Trasformar objeto em ebjeto JSON
        if serializer.is_valid(): # Verificar objeto está correto
            serializer.save() # Salvar objeto
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE']) # Função decorator com argumentos (GET e PUT e DELETE)
def todo_detail_change_and_delete(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializers(todo, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)