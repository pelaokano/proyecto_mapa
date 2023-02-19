from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from modelo_datos.views.views import inicial
from modelo_datos.views.views_lineas import LineaList

class InicialTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='pelaokano', email='pelaokano@mail.com', password='aalar009')

    def test_index_loads_properly(self):
        request = self.factory.get('')
        request.user = self.user
        response = inicial(request)
        
        self.assertEqual(response.status_code, 200)

class LineListTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='pelaokano', email='pelaokano@mail.com', password='aalar009')

    def test_index_loads_properly(self):
        request = self.factory.get('lineas/lista_lineas')
        request.user = self.user
        response = LineaList.as_view()(request)
        self.assertEqual(response.status_code, 200)