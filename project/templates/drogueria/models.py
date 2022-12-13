from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    droga = models.CharField(max_length=100)
    codigo = models.IntegerField()
    precio = models.IntegerField()

    def str(self):
        return f"{self.nombre},{self.droga},{self.codigo},{self.precio},{self.id}"
    nombre = models.CharField(max_length=100)