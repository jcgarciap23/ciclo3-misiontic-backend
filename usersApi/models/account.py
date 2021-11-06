from django.db import models
from usersApi.models.user import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, null=True)
    lastChangeDate = models.DateTimeField(null=True)
    isActive = models.BooleanField(default=True)
