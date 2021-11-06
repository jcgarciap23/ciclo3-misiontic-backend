import json
from django.http import response
from django.http.response import JsonResponse
from rest_framework.views import View, APIView
from servicesApi.models import Servicio

'''Crear servicios'''
class createServices(APIView):

    def post(self, request):

        Servicio.objects.create(
            name = request.POST.get('name'), 
            description = request.POST.get('description'),
            price_hour = request.POST.get('price_hour'),
            idproveedor_id = request.POST.get('idproveedor'),
            image = request.FILES['image']
        )
        response = {'message': f"Servicio creado correctamente"}
        return JsonResponse(response, status=201)


'''Listar todos los servicios'''
class findServices(APIView):

    def get(self, request):
        services = list(Servicio.objects.values())
        if(len(services)>0):
            response = {'servicios': services}
            return JsonResponse(response)
        else:
            response = {'message': f"Servicios no encontrados"}
            return JsonResponse(response, status=404)


'''Listar todos los servicios de un PROVEEDOR'''
class findServicesByProveedor(APIView):

    def get(self, request, id):
        services = list(Servicio.objects.filter(idproveedor_id=id).values())
        if(len(services)>0):
            response = {'servicios': services}
            return JsonResponse(response)
        else:
            response = {'message': f"Servicios del proveedor con id:{id} no encontrado"}
            return JsonResponse(response, status=404)
        

'''Buscar servicios por ID'''
class findByIdServices(APIView):

    def get(self, request, id):
        services = list(Servicio.objects.filter(idservice=id).values())
        if(len(services)>0):
            response = {'servicio': services[0]}
            return JsonResponse(response)
        else:
            response = {'message': f"Servicio con id:{id} no encontrado"}
            return JsonResponse(response, status=404)


'''Modificar servicios'''  
class updateServices(APIView):

    def put(self, request, id):
        data = json.loads(request.body)
        try:
            services = Servicio.objects.get(idservice=id)
            services.name = data['name']
            services.description = data['description']
            services.price_hour = data['price_hour']
            services.save()
            response = {'message': f"Servicio con id:{id} modificado correctamente"}
            return JsonResponse(response)
        except Servicio.DoesNotExist:
            response = {'message': f"Servicio con id:{id} no encontrado"}
            return JsonResponse(response, status=404)       
            
    
'''Eliminar servicios'''
class deleteServices(APIView):

    def delete(self, request, id):
        try:
            services = Servicio.objects.get(idservice=id)
            services.delete()
            response = {'message': f"Servicio con id:{id} eliminado correctamente"}
            return JsonResponse(response)
        except Servicio.DoesNotExist:
            response = {'message': f"Servicio con id:{id} no encontrado"}
            return JsonResponse(response, status=404) 
