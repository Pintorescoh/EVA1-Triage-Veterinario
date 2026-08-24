from django.contrib import admin
from django.urls import path
from recepcion import views  # Importamos tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea conecta la página principal (vacía '') con tu función sala_espera
    path('', views.sala_espera, name='sala_espera'), 
]