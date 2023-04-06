from django.db import models

# Create your models here.
class Topico(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    texto = models.CharField(max_length=200)
    data_adcionada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.texto 
    
class Entrada(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    data_adcionada = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ela nos permite definir um atributo especial que diz a Django para usar Entries quando precisar se referir a mais de uma entrada."""
        verbose_name_plural = "Entradas"

    def __str__(self):
        """quais informações devem ser mostradas quando entradas individuais forem referenciadas."""
        return self.texto[:50] + "..."
    

