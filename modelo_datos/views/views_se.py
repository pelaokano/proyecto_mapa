from modelo_datos.models import Subestacion
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

# Create your views here.
@method_decorator(login_required(login_url='login_user'), name='dispatch')
class SubestacionList(ListView):
    model = Subestacion
    ordering = "id"
    paginate_by = 10
    template_name = "list_subestaciones.html"
    context_object_name = "subestaciones"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class SubestacionDetail(DetailView):
    model = Subestacion
    template_name = "detail_subestacion.html"
    context_object_name = "subestacion"

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_se'), name='dispatch')
class SubestacionDelete(DeleteView):
    model = Subestacion
    success_url = reverse_lazy("lista_se")
    template_name = "confirm_delete.html"
