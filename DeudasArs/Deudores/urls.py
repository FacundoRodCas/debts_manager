from django.urls import path
from .views import mostrar_deudores, crear_deuda, modificar_deuda, eliminar_deuda

app_name = "deudores"
urlpatterns = [
    path('deudores/', mostrar_deudores, name=""),
    path('crear/', crear_deuda, name="crear"),
    path('modificar/<int:pk>', modificar_deuda, name="modificar"),
    path('eliminar/<int:pk>', eliminar_deuda, name="eliminar")
]