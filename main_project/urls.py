from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/services/', include('servicesApi.routes')),
    path('api/users/', include('usersApi.routes')),
    path('api/pedido/', include('pedidoApi.routes')),
    path('api/carrito/', include('carritoApi.routes')),
]
