from django.urls import path
from pedidoApi.views import createPedido, findPedidoByCliente, findPedidoByProveedor, changeStatus, findByFacture

urlpatterns = [
   path('create/', createPedido.as_view()),                          #Crear pedido
   path('buscarxProv/<int:id>/', findPedidoByProveedor().as_view()), #Buscar pedidos por proveedor
   path('buscarxCli/<int:id>/', findPedidoByCliente().as_view()),    #buscar pedidos por cliente
   path('modificarStatus/<int:id>/', changeStatus().as_view()),      #Modificar estado
   path('buscarFactura/<int:number>/', findByFacture().as_view()),   #Buscar por factura
]