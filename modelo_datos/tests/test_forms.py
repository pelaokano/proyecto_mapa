from django.test import TestCase

from modelo_datos.forms import PuntoForm

class PuntoFormTest(TestCase):
    
    def test_form_help_text(self):
        form = PuntoForm()
        self.assertEqual(form.fields['longitud'].help_text, 'Se deben ingresar en coordenadas decimales')
        self.assertEqual(form.fields['latitud'].help_text, 'Se deben ingresar en coordenadas decimales')

    def test_form_valid(self):
        data = {
            'nombre_punto': 'punto_santiago',
            'longitud': -70.64827,
            'latitud': -33.45694
        }
        form = PuntoForm(data=data)
        self.assertEqual(form.is_valid(), True)