from django.urls import path
from modelo_datos.views.views_se import SubestacionList, SubestacionDetail, SubestacionDelete
from modelo_datos.views.views_lineas import LineaList, LineaDetail, LineaDelete
from modelo_datos.views.views_puntos import PuntoList, PuntoDetail, PuntoDelete
from modelo_datos.views.views import inicial, PuntoCreateViewForm, PuntoUpdateViewForm, SECreateViewForm, SEUpdateViewForm, prueba
from modelo_datos.views.views import LineaCreateViewForm, LineaUpdateViewForm, PropietarioCreateViewForm, PropietarioUpdateViewForm
from modelo_datos.views.views_propietario import PropietarioList, PropietarioDetail, PropietarioDelete


urlpatterns = [
    path('', inicial, name="home"),
    path('prueba', prueba, name="prueba"),
    
    path('sub/lista_se', SubestacionList.as_view(), name="lista_se"),
    path('sub/<int:pk>', SubestacionDetail.as_view(), name="detalle_se"),
    path("sub/update/<int:pk>", SEUpdateViewForm.as_view(), name="update_subestacion"),
    path("sub/delete/<int:pk>", SubestacionDelete.as_view(), name="delete_subestacion"),
    path("sub/create", SECreateViewForm.as_view(), name="create_subestacion"),
    
    path('lineas/lista_lineas', LineaList.as_view(), name="lista_lineas"),
    path('lineas/<int:pk>', LineaDetail.as_view(), name="detalle_linea"),
    path("lineas/update/<int:pk>", LineaUpdateViewForm.as_view(), name="update_lineas"),
    path("lineas/delete/<int:pk>", LineaDelete.as_view(), name="delete_lineas"),
    path("lineas/create", LineaCreateViewForm.as_view(), name="create_lineas"),
    
    path('puntos/lista_lineas', PuntoList.as_view(), name="lista_puntos"),
    path('puntos/<int:pk>', PuntoDetail.as_view(), name="detalle_puntos"),
    path("puntos/update/<int:pk>", PuntoUpdateViewForm.as_view(), name="update_puntos"),
    path("puntos/delete/<int:pk>", PuntoDelete.as_view(), name="delete_puntos"),
    path("puntos/create", PuntoCreateViewForm.as_view(), name="create_puntos"),
    
    path('propietario/lista_propietario', PropietarioList.as_view(), name="lista_propietario"),
    path('propietario/<int:pk>', PropietarioDetail.as_view(), name="detalle_propietario"),
    path("propietario/update/<int:pk>", PropietarioUpdateViewForm.as_view(), name="update_propietarios"),
    path("propietario/delete/<int:pk>", PropietarioDelete.as_view(), name="delete_propietarios"),
    path("propietario/create", PropietarioCreateViewForm.as_view(), name="create_propietarios"),

]