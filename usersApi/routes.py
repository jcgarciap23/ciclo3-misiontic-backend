from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from usersApi.views import UserCreateView, UserDetailView, findSaldo, recargarSaldo, disminuirSaldo

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),                      #Loguear Usuario
    path('refresh/', TokenRefreshView.as_view()),                       #Renovar acceso al token
    path('user/', UserCreateView.as_view()),                            #Registrar Usuario
    path('user/<int:pk>/', UserDetailView.as_view()),                   #Obtener información del Usuario
    path('user/versaldo/<int:id>/', findSaldo.as_view()),               #Obtener saldo del Cliente
    path('user/recargarsaldo/<int:id>/', recargarSaldo.as_view()),      #Recargar saldo del Cliente
    path('user/restarsaldo/<int:id>/', disminuirSaldo.as_view()),       #Disminuir saldo del Cliente
]