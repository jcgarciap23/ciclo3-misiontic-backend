import json
from django.http.response import JsonResponse
from rest_framework.views import APIView
from pedidoApi.models import Pedido
from servicesApi.models import Servicio

class createPedido(APIView):

    def post(self, request):
        data = json.loads(request.body)
        '''id = data['idservice']
        services = Servicio.objects.get(idservice=id)
        print(services.price_hour)'''
        Pedido.objects.create(
            name = data['name'], 
            total = data['total'],
            totalHours = data['totalHours'],
            idproveedor = data['idproveedor'],
            idservicio_id = data['idservicio'],
            idpcliente_id = data['idcliente'],
        )
        response = {'message': f"Servicio {data['name']} creado correctamente"}
        return JsonResponse(response, status=201)

class findPedidoByCliente(APIView):
    def get(self, request, id):
        pedido = list(Pedido.objects.filter(idpcliente_id=id).values())
        if(len(pedido)>0):
            response = {'Pedidos': pedido}
            return JsonResponse(response)
        else:
            response = {'message': f"Pedidos del cliente con id:{id} no encontrado"}
            return JsonResponse(response, status=404)

class findPedidoByProveedor(APIView):
    def get(self, request, id):
        pedido = list(Pedido.objects.filter(idproveedor=id).values())
        if(len(pedido)>0):
            response = {'Pedidos': pedido}
            return JsonResponse(response)
        else:
            response = {'message': f"Pedidos del Servidor con id:{id} no encontrado"}
            return JsonResponse(response, status=404)

class changeStatus(APIView):
    def put(self, request, id):
        data = json.loads(request.body)
        try:
            pedido = Pedido.objects.get(idpedido=id)
            pedido.status = data['status']
            pedido.save()
            response = {'message': f"Estado del pedido con id:{id} modificado correctamente"}
            return JsonResponse(response)
        except Servicio.DoesNotExist:
            response = {'message': f"Pedido con id:{id} no encontrado"}
            return JsonResponse(response, status=404) 

class findByFacture(APIView):
    def get(self, request, number):
        pedido = list(Pedido.objects.filter(invoiceNumber=number).values())
        if(len(pedido)>0):
            response = {'Pedidos': pedido}
            return JsonResponse(response)
        else:
            response = {'message': f"Pedidos del Servidor con id:{id} no encontrado"}
            return JsonResponse(response, status=404)