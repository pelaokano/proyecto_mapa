from math import radians, cos, sin, asin, acos, sqrt, pi
import numpy as np

class PuntosFiltrados:
    def __init__(self, puntos, latitud, longitud, distancia):
        self.puntos = puntos
        self.latitud = latitud
        self.longitud = longitud
        self.distancia = distancia
        self.filtro_punto = []
        self.filtro_sub = []
        self.filtro_linea = []
        
    def spherical_distance(self, lat1, lon1, lat2, lon2, r=6371):
        coordinates = lat1, lon1, lat2, lon2
        phi1, lambda1, phi2, lambda2 = [radians(c) for c in coordinates]  
        a = (np.square(sin((phi2-phi1)/2)) + cos(phi1) * cos(phi2) * np.square(sin((lambda2-lambda1)/2)))
        d = 2*r*asin(np.sqrt(a))
        return d
        
    def filtrar(self):
        self.filtro_punto=[p for p in self.puntos if self.spherical_distance(self.latitud, self.longitud, p.latitud, p.longitud) <= self.distancia]
        self.filtro_sub=[p.get_sub.all()[0] for p in self.filtro_punto if len(p.get_sub.all())]
        self.filtro_linea=list(set([p.get_linea.all()[0] for p in self.filtro_punto if len(p.get_linea.all())]))
        return self.filtro_sub, self.filtro_linea

class GeojsonSE:
    def __init__(self, subestaciones):
        self.subestaciones = subestaciones
        self.geojson = {'type': 'FeatureCollection', 'features': []}
        
    def feature_se(self, se):
        feature = {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': []}}
        feature['geometry']['coordinates'] = [se.id_punto.longitud, se.id_punto.latitud]
        feature['properties']['nombre'] = se.nombre_subestacion
        feature['properties']['id'] = se.id_subestacion
        feature['properties']['url_se'] = se.url_subestacion
        feature['properties']['region'] = se.get_region_display()
        return feature

    def desplegar(self):
        self.geojson['features'] = [self.feature_se(se) for se in self.subestaciones]
        return self.geojson
    
class GeojsonLinea:
    def __init__(self, lineas):
        self.lineas = lineas
        self.geojson = {'type': 'FeatureCollection', 'features': []}

    def feature_linea(self, linea):
        feature = {'type': 'Feature','properties': {}, 'geometry': {'type':'LineString','coordinates':[]}}
        feature['geometry']['coordinates'] = [[punto.longitud, punto.latitud] for punto in linea.puntos.all()]
        feature['properties']['nombre'] = linea.nombre_linea
        feature['properties']['tension'] = linea.tension
        feature['properties']['largo'] = linea.largo
        return feature

    def desplegar(self):
        self.geojson['features'] = [self.feature_linea(linea) for linea in self.lineas]
        return self.geojson