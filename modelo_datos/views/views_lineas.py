from modelo_datos.models import Linea
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

# Create your views here.

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class LineaList(ListView):
    model = Linea
    ordering = "id"
    paginate_by = 10
    template_name = "list_lineas.html"
    context_object_name = "lineas"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class LineaDetail(DetailView):
    model = Linea
    template_name = "detail_linea.html"
    context_object_name = "linea"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_lineas'), name='dispatch')
class LineaDelete(DeleteView):
    model = Linea
    success_url = reverse_lazy("lista_lineas")
    template_name = "confirm_delete.html"
