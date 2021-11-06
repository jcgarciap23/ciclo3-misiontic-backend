from django.urls import path
from servicesApi.views import findServices, findByIdServices, createServices, updateServices, deleteServices, findServicesByProveedor

urlpatterns = [
    path('list/', findServices.as_view()),                                  #Buscar todos los servicios
    path('list/<int:id>/', findByIdServices.as_view()),                     #Buscar servicios por id
    path('listByProveedor/<int:id>/', findServicesByProveedor.as_view()),   #Buscar servicios por Proveedor
    path('create/', createServices.as_view()),                              #Crear servicio
    path('update/<int:id>/', updateServices.as_view()),                     #Modificar servicio
    path('delete/<int:id>/', deleteServices.as_view()),                     #Eliminar servicio 
]