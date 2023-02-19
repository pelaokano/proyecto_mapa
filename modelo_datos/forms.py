from django.forms import ModelForm
from modelo_datos.models import Punto, Subestacion, Linea, Propietario
from django.core.exceptions import ValidationError

#form para puntos
class PuntoForm(ModelForm):
    class Meta:
        model = Punto
        fields = ['nombre_punto', 'longitud', 'latitud']
        help_texts = {
            'longitud': 'Se deben ingresar en coordenadas decimales',
            'latitud': 'Se deben ingresar en coordenadas decimales'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        nombre_punto = cleaned_data.get('nombre_punto')
        longitud = cleaned_data.get('longitud')
        latitud  = cleaned_data.get('latitud')

        if longitud == 0:
            raise ValidationError( "Longitud debe ser distinto de cero" )
            
        if latitud == 0:
            raise ValidationError( "Latitud debe ser distinto de cero" )
            
        if len(nombre_punto) < 2:
            raise ValidationError( "El nombre del punto debe tener una extension mayor a 1 caracter" )
            
        if len(nombre_punto) > 20:
            raise ValidationError( "El nombre del punto debe tener una extension menor a 20 caracteres" )

#form para subestaciones
class SEForm(ModelForm):
    class Meta:
        model = Subestacion
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        
        nombre_subestacion = cleaned_data.get('nombre_subestacion')
        url_subestacion = cleaned_data.get('url_subestacion')
        id_subestacion  = cleaned_data.get('id_subestacion')
        id_punto = cleaned_data.get('id_punto')
        region = cleaned_data.get('region')
        propietario = cleaned_data.get('propietario')
        
        if Subestacion.objects.filter(nombre_subestacion=nombre_subestacion).count() > 0:
            raise ValidationError( "El nombre debe ser distinto al de una subestacion ya registrada")
        
        if Subestacion.objects.filter(id_subestacion=id_subestacion).count() > 0:
            raise ValidationError( "El ID de la subestacion debe ser distinto al de una subestacion ya registrada")

#form para lineas
class LineaForm(ModelForm):
    class Meta:
        model = Linea
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        
        nombre_linea = cleaned_data.get('nombre_linea')
        largo = cleaned_data.get('largo')
        tension  = cleaned_data.get('tension')
        puntos = cleaned_data.get('puntos')
        propietario = cleaned_data.get('propietario')
        
        if Linea.objects.filter(nombre_linea=nombre_linea).count() > 0:
            raise ValidationError( "El nombre debe ser distinto al de una linea ya registrada")
            
#form para propietario
class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        
        nombre = cleaned_data.get('nombre')
        
        if Propietario.objects.filter(nombre=nombre).count() > 0:
            raise ValidationError( "El nombre debe ser distinto al de un propietario ya registrada")            