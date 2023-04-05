from django.db import models

# Create your models here.
class topico(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""

    texto = models.CharField(max_length=200)
    data_adcionada = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.texto 

