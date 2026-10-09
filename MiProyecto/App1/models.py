from django.db import models

# Create your models here.

from django.db import models

class BitacoraGestion(models.Model):
    codigo_unidad = models.CharField(max_length=20, verbose_name="Código de Unidad")
    observacion = models.CharField(max_length=255, verbose_name="Observación General")
    kilometraje = models.IntegerField(verbose_name="Kilometraje Actual")
    revisado_mecanica = models.BooleanField(default=False, verbose_name="¿Revisión Mecánica Aprobada?")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def __str__(self):
        return f"Registro {self.codigo_unidad} - {self.fecha_registro.strftime('%d/%m/%Y')}"