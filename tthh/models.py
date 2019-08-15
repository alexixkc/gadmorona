from django.db import models

# Create your models here.
class TipoAusencia(models.Model):
	"""docstring for TipoAusencia"""
	ausencia = models.CharField(max_length=100)
	activo = models.BooleanField()

	def __str__(self):
		return self.ausencia

class Empleado(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)

	def __str__(self):
		return self.nombres+ " "+self.apellidos
		

class Registro(models.Model):

	tipo_ausencia = models.ForeignKey(TipoAusencia,on_delete=models.CASCADE)
	empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE,blank=True)
	fecha_desde = models.DateField('Desde')
	fecha_hasta = models.DateField('Hasta')
	numero_dias = models.IntegerField()

	def __str__(self):
		return self.empleado.nombres
		