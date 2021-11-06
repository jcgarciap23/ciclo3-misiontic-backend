from django.db import models
from servicesApi.models import Servicio
from usersApi.models.user import User
from django.utils.timezone import now
import datetime

class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True, null=False)
    idservicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.CASCADE)
    idpcliente = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    idproveedor = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=40, null=False)
    total = models.FloatField(null=False, default=0)
    totalHours = models.FloatField(null=False, default=0)
    date = models.DateField(null=False, default=now)
    option = [
        ('1', 'Por hacer'),
        ('2' ,'En proceso'),
        ('3', 'Terminado')
    ]
    status = models.CharField(max_length=1, choices=option, default='1')
    

