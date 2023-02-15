from modelo_datos.models import Punto
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
# Create your views here.

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class PuntoList(ListView):
    model = Punto
    ordering = "id"
    paginate_by = 10
    template_name = "list_puntos.html"
    context_object_name = "puntos"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class PuntoDetail(DetailView):
    model = Punto
    template_name = "detail_punto.html"
    context_object_name = "punto"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_puntos'), name='dispatch')
class PuntoDelete(DeleteView):
    model = Punto
    success_url = reverse_lazy("lista_puntos")
    template_name = "confirm_delete.html"
