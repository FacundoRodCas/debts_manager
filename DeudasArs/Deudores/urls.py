from django.urls import path
from .views import mostrar_deudores, crear_deuda
app_name = "deudores"
urlpatterns = [
    path('deudores/', mostrar_deudores, name=""),
    path('crear/', crear_deuda, name="crear"),
]