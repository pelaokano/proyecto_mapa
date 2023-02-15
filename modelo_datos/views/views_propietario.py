from modelo_datos.models import Propietario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
# Create your views here.

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class PropietarioList(ListView):
    model = Propietario
    ordering = "id"
    paginate_by = 10
    template_name = "list_propietario.html"
    context_object_name = "propietarios"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class PropietarioDetail(DetailView):
    model = Propietario
    template_name = "detail_propietario.html"
    context_object_name = "propietario"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_propietario'), name='dispatch')
class PropietarioDelete(DeleteView):
    model = Propietario
    success_url = reverse_lazy("lista_propietario")
    template_name = "confirm_delete.html"
