from django.test import TestCase
from modelo_datos.models import Punto, Propietario, Subestacion

class PuntoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Punto.objects.create(nombre_punto='Punto_Santiago', latitud=-33.45694, longitud=-70.64827)

    def test_nombre_punto_max_length(self):
        punto = Punto.objects.get(id=1)
        max_length = punto._meta.get_field('nombre_punto').max_length
        self.assertEqual(max_length, 100)

    def test_str_nombre_punto(self):
        punto = Punto.objects.get(id=1)
        nombre_esperado = f'{punto.nombre_punto}'
        self.assertEqual(str(punto), nombre_esperado)

class PropietarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Propietario.objects.create(nombre='Propietario1')
        
    def test_nombre_propietario_max_length(self):
        propietario = Propietario.objects.get(id=1)
        max_length = propietario._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 100)
        
    def test_str_nombre_propietario(self):
        propietario = Propietario.objects.get(id=1)
        nombre_esperado = f'{propietario.nombre}'
        self.assertEqual(str(propietario), nombre_esperado)

class SEModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Punto.objects.create(nombre_punto='Punto_Santiago', latitud=-33.45694, longitud=-70.64827)
        Propietario.objects.create(nombre='Propietario1')
        punto = Punto.objects.get(id=1)
        propietario = Propietario.objects.get(id=1)
        Subestacion.objects.create(
        nombre_subestacion='SE_santiago',
        url_subestacion='URL',
        id_subestacion=1,
        id_punto=punto,
        region='11',
        propietario=propietario
        )

    def test_nombre_SE_max_length(self):
        subestacion = Subestacion.objects.get(id=1)
        max_length = subestacion._meta.get_field('nombre_subestacion').max_length
        self.assertEqual(max_length, 100)
        
    def test_str_nombre_SE(self):
        subestacion = Subestacion.objects.get(id=1)
        nombre_esperado = f'{subestacion.nombre_subestacion}'
        self.assertEqual(str(subestacion), nombre_esperado)

