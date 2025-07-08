from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.URLField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    
    class Meta:
        db_table = 'ProductosTabla'

    def __str__(self):
        return self.nombre
