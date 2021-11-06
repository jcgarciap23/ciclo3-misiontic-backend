import json
from django.http.response import JsonResponse
from rest_framework.views import APIView
from servicesApi.models import Servicio

class crearCarrito(APIView):
    
    lista=list()

    def post(self, request):
        data=json.loads(request.body)
        servicio=Servicio.objects.get(idservice=data['idservicio'])
        carrito = {
            'idservicio':data['idservicio'],
            'servicio':servicio.name,
            'horas':data['horas'],
            'precioxhora':servicio.price_hour,
            'totalxservicio': float(data['horas'])*float(servicio.price_hour),      
        }
        self.lista.append(carrito)
        mensaje={'carrito':carrito}
        return JsonResponse(mensaje)

    def get(self, request):             
        mensaje={'carrito':self.lista}
        return JsonResponse(mensaje)

    def delete(self, request, id):
        if id==0:
            self.lista.clear()
            mensaje={'carrito':self.lista}
            return JsonResponse(mensaje)
        '''for i in range(1,len(self.lista)):
            if id == self.lista[i]['idservicio']:
                self.lista[0]=self.lista[0]-self.lista[i]['totalxservicio']
                self.lista.pop(i)'''
        mensaje={'carrito':self.lista}
        return JsonResponse(mensaje)
    

        


