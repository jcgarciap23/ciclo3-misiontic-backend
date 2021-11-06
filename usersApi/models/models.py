from django.db import models

class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=40, null=False)
    email = models.CharField(max_length=200, null=False)
    role = models.IntegerField(null=True, default=1)

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=40, null=False)
    email = models.CharField(max_length=200, null=False)
    saldo = models.FloatField(default=0, null=False)
    role = models.IntegerField(null=True, default=0)