from django.urls import path
from webservice import views
from webservice.views import show_register
from webservice.api.register_api import register_user
from .views import obtener_productos_carrito_json
from webservice.api.login_api import login_api
from webservice.views import logout_view


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path("api/register/", register_user, name="register_user"),
    path('mostrar-registro/', show_register, name='show_register'),
    path('api/login/', login_api, name='login_api'),
    path('logout/', logout_view, name='logout'),

    # Nuevas rutas para el carrito de compras
    path('productos/', views.lista_productos, name='lista_productos'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('reducir/<int:producto_id>/', views.reducir_cantidad, name='reducir_cantidad'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('pagar/', views.pagar_con_mercado_pago, name='pagar'),
    path('pago-exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('pago-fallido/', views.pago_fallido, name='pago_fallido'),
    path('pago-pendiente/', views.pago_pendiente, name='pago_pendiente'),
    path('api/carrito/', obtener_productos_carrito_json, name='api_carrito'),
]
