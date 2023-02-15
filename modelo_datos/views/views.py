from modelo_datos.forms import PuntoForm, SEForm, LineaForm, PropietarioForm
from django.views.generic.edit import CreateView, UpdateView
from modelo_datos.models import Punto, Subestacion, Linea, Propietario
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

@permission_required('modelo_datos.editar', login_url='login_user')
#@permission_required('modelo_datos.add_punto', login_url='/login_user')
def prueba(request):
    return render(request, 'prueba.html')

@login_required(login_url='login_user')
def inicial(request):
    return render(request, 'index.html')

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_puntos'), name='dispatch')
class PuntoCreateViewForm(CreateView):
    model = Punto
    template_name = 'form_tipo.html'
    form_class = PuntoForm
    success_url = reverse_lazy("lista_puntos")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Punto'
        return context

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_puntos'), name='dispatch')
class PuntoUpdateViewForm(UpdateView):
    model = Punto
    template_name = 'form_tipo.html'
    form_class = PuntoForm
    success_url = reverse_lazy("lista_puntos")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Punto'
        return context
    
#vista para crear y editar subestaciones
@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_se'), name='dispatch')
class SECreateViewForm(CreateView):
    model = Subestacion
    template_name = 'form_tipo.html'
    form_class = SEForm
    success_url = reverse_lazy("lista_se")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Subestacion'
        return context

@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_se'), name='dispatch')
class SEUpdateViewForm(UpdateView):
    model = Subestacion
    template_name = 'form_tipo.html'
    form_class = SEForm
    success_url = reverse_lazy("lista_se")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Subestacion'
        return context

#vista para crear y editar lineas
@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_lineas'), name='dispatch')
class LineaCreateViewForm(CreateView):
    model = Linea
    template_name = 'form_tipo.html'
    form_class = LineaForm
    success_url = reverse_lazy("lista_lineas")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Linea'
        return context

@method_decorator(login_required(login_url='login_user'), name='dispatch')  
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_lineas'), name='dispatch')
class LineaUpdateViewForm(UpdateView):
    model = Linea
    template_name = 'form_tipo.html'
    form_class = LineaForm
    success_url = reverse_lazy("lista_lineas")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Linea'
        return context

#vista para crear y editar propietarios
@method_decorator(login_required(login_url='login_user'), name='dispatch')
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_propietario'), name='dispatch')
class PropietarioCreateViewForm(CreateView):
    model = Propietario
    template_name = 'form_tipo.html'
    form_class = PropietarioForm
    success_url = reverse_lazy("lista_propietario")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Propietario'
        return context
        
@method_decorator(login_required(login_url='login_user'), name='dispatch')  
@method_decorator(permission_required('modelo_datos.editar', login_url='lista_propietario'), name='dispatch')
class PropietarioUpdateViewForm(UpdateView):
    model = Propietario
    template_name = 'form_tipo.html'
    form_class = PropietarioForm
    success_url = reverse_lazy("lista_propietario")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_objeto'] = 'Propietario'
        return context