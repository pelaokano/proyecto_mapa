from django.urls import path
from .views import vista_puntos, enviar_geojsonSE2, enviar_geojsonLinea2

urlpatterns = [
    path('puntos', vista_puntos, name='list_puntos'),
    path('geojson_puntosSE2', enviar_geojsonSE2, name="geojson_puntosSE2"),
    path('enviar_geojsonLinea2', enviar_geojsonLinea2, name="enviar_geojsonLinea2"),
    ]
