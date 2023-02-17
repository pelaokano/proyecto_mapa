from django.shortcuts import render
from modelo_datos.models import Punto, Subestacion, Linea
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from .serializers import puntoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .clases import PuntosFiltrados, GeojsonSE, GeojsonLinea

# Create your views here.

@api_view(['GET', 'POST'])
def vista_puntos(request):
    if request.method == 'GET':
        puntos = Punto.objects.all()
        serializer_punto = puntoSerializer(puntos, many=True)
        return Response(serializer_punto.data)

# def enviar_geojsonSE(request):
    # subestaciones = Subestacion.objects.all()
    # geojsonSE = {'type': 'FeatureCollection', 'features': []}

    # for se in subestaciones:
        # feature = {'type': 'Feature', 
                   # 'properties': {},
                   # 'geometry': {'type':'Point',
                                # 'coordinates':[]}}

        # feature['geometry']['coordinates'] = [se.id_punto.longitud, se.id_punto.latitud]
        # feature['properties']['nombre'] = se.nombre_subestacion
        # feature['properties']['id'] = se.id_subestacion
        # feature['properties']['url_se'] = se.url_subestacion
        # feature['properties']['region'] = se.get_region_display()
        # geojsonSE['features'].append(feature)
    
    # return JsonResponse(geojsonSE)

# def enviar_geojsonLinea(request):
    # #lineas = Linea.objects.get(pk=1)
    # lineas = Linea.objects.all()
    # geojsonLinea = {'type': 'FeatureCollection', 'features': []}

    # for linea in lineas:
        # feature = {'type': 'Feature', 
                   # 'properties': {},
                   # 'geometry': {'type':'LineString',
                                # 'coordinates':[]}}

        # for punto in linea.puntos.all():
            # feature['geometry']['coordinates'].append([punto.longitud, punto.latitud])
        
        # feature['properties']['nombre'] = linea.nombre_linea
        # feature['properties']['tension'] = linea.tension
        # feature['properties']['largo'] = linea.largo
        # geojsonLinea['features'].append(feature)

    # return JsonResponse(geojsonLinea)

#@csrf_exempt
def enviar_geojsonSE2(request):   
    geojsonSE = {'type': 'FeatureCollection', 'features': []}
    
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        print(data)
        valorCriterio = data.get('region')
        print(valorCriterio)
        subestaciones = Subestacion.objects.all()

        for se in subestaciones:
            if se.get_region_display() == valorCriterio:
                feature = {'type': 'Feature', 
                           'properties': {},
                           'geometry': {'type':'Point',
                                        'coordinates':[]}}

                feature['geometry']['coordinates'] = [se.id_punto.longitud, se.id_punto.latitud]
                feature['properties']['nombre'] = se.nombre_subestacion
                feature['properties']['id'] = se.id_subestacion
                feature['properties']['url_se'] = se.url_subestacion
                feature['properties']['region'] = se.get_region_display()
                geojsonSE['features'].append(feature)
        
    if len(geojsonSE['features']) == 0:
        geojsonSE={'resultados':'no se encontraron resultados para el criterio'}

    return JsonResponse(geojsonSE)

#@csrf_exempt
def enviar_geojsonLinea2(request):
    print(get_token(request))
    geojsonLinea = {'type': 'FeatureCollection', 'features': []}
    if request.method == 'POST': 
        data = request.POST
        print('prueba')
        print(data)
        criterioValor = data.get('tension')
        print(criterioValor)
        lineas = Linea.objects.filter(tension=criterioValor)

        for linea in lineas:
            feature = {'type': 'Feature', 
                       'properties': {},
                       'geometry': {'type':'LineString',
                                    'coordinates':[]}}

            for punto in linea.puntos.all():
                feature['geometry']['coordinates'].append([punto.longitud, punto.latitud])
            
            feature['properties']['nombre'] = linea.nombre_linea
            feature['properties']['tension'] = linea.tension
            feature['properties']['largo'] = linea.largo
            geojsonLinea['features'].append(feature)
    
    if len(geojsonLinea["features"]) == 0:
        geojsonLinea={'resultados':'no se encontraron resultados para el criterio'}

    return JsonResponse(geojsonLinea)

def enviar_geojsonFiltroPunto(request):
    if request.method == 'POST': 
        data = request.POST
        lat=float(data.get('latitud'))
        lon=float(data.get('longitud'))
        dist=float(data.get('distancia'))
        puntos=Punto.objects.all()
        puntos_filtro = PuntosFiltrados(puntos, lat, lon, dist)
        ssee, lineas = puntos_filtro.filtrar()
        geojsonSE = GeojsonSE(ssee)
        geojsonLinea = GeojsonLinea(lineas)
        
        geojsonTotal = {
            'SSEE': geojsonSE.desplegar(),
            'Lineas': geojsonLinea.desplegar()
        
        }
        
    return JsonResponse(geojsonTotal)

