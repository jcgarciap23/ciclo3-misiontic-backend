from django.contrib import admin
from usersApi.models.models import Cliente, Proveedor
from usersApi.models.user import User
from usersApi.models.account import Account

admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(User)
admin.site.register(Account)
