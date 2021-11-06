from rest_framework.views import APIView
from usersApi.models.user import User
from django.http.response import JsonResponse
import json

'''Buscar saldo de CLiente por ID'''
class findSaldo(APIView):

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            response = {'saldo': user.saldo}
            return JsonResponse(response)
        except User.DoesNotExist:
            response = {'message': f"CLiente con id:{id} no encontrado"}
            return JsonResponse(response, status=404) 

'''Modificar servicios'''  
class recargarSaldo(APIView):

    def put(self, request, id):
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=id)
            saldoTotal= float(user.saldo)+float(data['saldo'])
            user.saldo = saldoTotal
            user.save()
            response = {'saldo': user.saldo}
            return JsonResponse(response)
        except User.DoesNotExist:
            response = {'message': f"Cliente con id:{id} no encontrado"}
            return JsonResponse(response, status=404) 

class disminuirSaldo(APIView):

    def put(self, request, id):
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=id)
            saldoTotal= float(user.saldo)-float(data['saldo'])
            user.saldo = saldoTotal
            user.save()
            response = {'saldo': user.saldo}
            return JsonResponse(response)
        except User.DoesNotExist:
            response = {'message': f"Cliente con id:{id} no encontrado"}
            return JsonResponse(response, status=404) 

