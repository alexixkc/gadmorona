from django.contrib import admin
from tthh.models import *

# Register your models here.
admin.site.register(TipoAusencia)
admin.site.register(Registro)
admin.site.register(Empleado)

class RegistroAdmin(admin.ModelAdmin):
    #readonly_fields = ('created', 'updated')
    list_display = ('empleado', 'tipo_ausencia')