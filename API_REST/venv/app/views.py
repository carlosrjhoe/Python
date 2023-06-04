from .models import Todo
from .serializers import TodoSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
# from rest_framework import generics

class TodoListAndCreate(APIView):
    def get(self, request):
        """Pegar todos os objetos e listar"""
        todo = Todo.objects.all() 
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Verificar e Criar um objeto e transformar em objeto JSON"""
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailChangeAndDelete(APIView):

    def get_object(self, pk):
        """Verificar se objeto existe, caso contrário, retorna um erro."""
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializers(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        """Atualizar objeto"""
        todo = self.get_object(pk=pk)
        serializer = TodoSerializers(todo, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deletar objeto"""
        todo = self.get_object(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)