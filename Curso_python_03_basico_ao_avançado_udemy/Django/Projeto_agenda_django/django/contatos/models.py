from django.utils import timezone
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.nome}'
    
    
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    date_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nome}'
    

    