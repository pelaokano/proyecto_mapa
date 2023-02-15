from django.contrib import admin
from modelo_datos.models import Punto, Subestacion, Linea, Propietario
# Register your models here.

admin.site.register(Punto)
admin.site.register(Subestacion)
admin.site.register(Linea)
admin.site.register(Propietario)
