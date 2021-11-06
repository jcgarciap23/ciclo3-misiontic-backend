from django.urls import path
from carritoApi.views import crearCarrito

urlpatterns = [
    path('metodos/', crearCarrito.as_view()),                       #Métodos de ingresar servicios y mostrar servicios al carrito
    path('eliminarServicios/<int:id>/', crearCarrito.as_view()),    #Eliminar servicios del carrito y vaciar carrito
]