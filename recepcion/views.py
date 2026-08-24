from django.shortcuts import render
import json
import os
from django.conf import settings

def sala_espera(request):
    # 1. Le decimos a Django dónde está exactamente tu archivo datos.json
    # (Lo busca en la carpeta principal de tu proyecto)
    ruta_archivo = os.path.join(settings.BASE_DIR, 'datos.json')
    
    lista_pacientes = []
    
    # 2. Si el archivo existe, lo abre y carga los pacientes
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            try:
                lista_pacientes = json.load(archivo)
            except json.JSONDecodeError:
                lista_pacientes = [] # Si el archivo está vacío, no falla
                
    # 3. Empaqueta los pacientes y se los envía a una página web (HTML)
    contexto = {
        'pacientes': lista_pacientes
    }
    
    return render(request, 'recepcion/sala.html', contexto)
