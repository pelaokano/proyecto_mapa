from django.db import models

# Create your models here.

#clase para almacenar puntos con longitud y latitud
class Punto(models.Model):
    nombre_punto = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    longitud = models.FloatField()
    latitud = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "punto"
        verbose_name_plural = "puntos"
        ordering = ["nombre_punto"]

    def __str__(self):
        return self.nombre_punto

class Propietario(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "propietario"
        verbose_name_plural = "propietarios"

    def __str__(self):
        return self.nombre
    
class Subestacion(models.Model):
    #regiones de chile
    REGIONES = [
    ('3','antofagasta'),
    ('11','araucania'),
    ('1','arica-parinacota'),
    ('4','atacama'),
    ('10','biobio'),
    ('5','coquimbo'),
    ('13','los-lagos'),
    ('12','los-rios'),
    ('9','maule'),
    ('7','metropolitana'),
    ('16','nuble'),
    ('8','ohiggins'),
    ('2','tarapaca'),
    ('6','valparaiso')
    ]

    nombre_subestacion = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    url_subestacion = models.URLField(max_length = 200, null=False, blank=False)
    id_subestacion = models.IntegerField(null=False, blank=False)
    id_punto = models.ForeignKey(Punto, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=20,choices=REGIONES,null=True,blank=True,verbose_name="Region")
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")  
    
    class Meta:
        verbose_name = "subestacion"
        verbose_name_plural = "subestaciones"    
    
    def __str__(self):
        return self.nombre_subestacion

class Linea(models.Model):
    TENSIONES = [
        ("44", "44KV"),
        ("66", "66KV"),
        ("110", "110KV"),
        ("154", "154KV"),
        ("220", "220KV"),
        ("345", "345KV"),
        ("500", "500KV")
    ]  
    
    nombre_linea = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    largo = models.FloatField(null=False, blank=False)
    tension = models.CharField(max_length=20,choices=TENSIONES,null=True,blank=True,verbose_name="Tension")
    puntos = models.ManyToManyField(Punto, related_name="get_lineas")
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "linea"
        verbose_name_plural = "lineas"    

    def __str__(self):
        return self.nombre_linea
