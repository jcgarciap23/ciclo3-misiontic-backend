from django.db import models
from usersApi.models.user import User

class Servicio(models.Model):
    idservice = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=200, null=False)
    price_hour = models.FloatField(null=False)
    idproveedor = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)




