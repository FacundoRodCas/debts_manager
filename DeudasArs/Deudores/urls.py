from django.urls import path
from .views import mostrar_deudores

urlpatterns = [
    path('deudores/', mostrar_deudores),
]