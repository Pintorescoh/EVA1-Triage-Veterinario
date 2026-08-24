import json
import os
from tabulate import tabulate

# 1. Ingreso de Datos
nombre_mascota = input("Nombre paciente: ")
try:
    dificultad_respiratoria = int(input("¿Tiene ahogo o dificultad para respirar? (1=Sí, 0=No): "))
    nivel_dolor = int(input("Nivel de dolor aparente (1 al 10): "))
except ValueError:
    print("Error: Debes ingresar números enteros para la respiración y el dolor.")
    dificultad_respiratoria = -1
    nivel_dolor = -1

# 2. Motor de Decisiones (Triage)
if dificultad_respiratoria not in [0, 1] or nivel_dolor < 1 or nivel_dolor > 10:
    resultado = "Inválido"
    print("Error: Datos ingresados fuera de rango.")
elif dificultad_respiratoria == 1:
    resultado = "Código Rojo"
    print(f"Aceptado: Pase directo de Urgencia. {nombre_mascota} entra a Box de Reanimación (Código Rojo).")
elif nivel_dolor >= 6:
    resultado = "Código Amarillo"
    print(f"Aceptado: {nombre_mascota} entra a Box de Observación (Código Amarillo).")
else:
    resultado = "Código Verde"
    print(f"Aceptado: {nombre_mascota} espera su turno en Sala General (Código Verde).")

# 3. Empaquetar y guardar (Solo si el dato es válido)
if resultado != "Inválido":
    
    # Traducimos el número a texto antes de guardarlo
    if dificultad_respiratoria == 1:
        texto_respiracion = "Sí"
    else:
        texto_respiracion = "No"

    # Armamos el diccionario con nombres limpios para la web
    nuevo_paciente = {
        "Nombre": nombre_mascota,
        "Dificultad_Respiracion": texto_respiracion,
        "Dolor": nivel_dolor,
        "Gravedad": resultado
    }

    # Cargar datos existentes si el archivo ya tiene algo
    lista_pacientes = []
    if os.path.exists('datos.json'):
        with open('datos.json', 'r', encoding='utf-8') as archivo:
            try:
                lista_pacientes = json.load(archivo)
            except json.JSONDecodeError:
                lista_pacientes = []

    # Agregar el nuevo paciente y guardar
    lista_pacientes.append(nuevo_paciente)
    with open('datos.json', 'w', encoding='utf-8') as archivo:
        json.dump(lista_pacientes, archivo, indent=4, ensure_ascii=False)
        
    print("\n[+] ¡Registro guardado exitosamente en el sistema!")

# 4. Mostrar el estado de la sala SIEMPRE (fuera del if)
print("\n--- ESTADO ACTUAL DE LA SALA ---")

# Leemos el archivo nuevamente para mostrar la tabla actualizada (o la histórica si hubo un error)
pacientes_actuales = []
if os.path.exists('datos.json'):
    with open('datos.json', 'r', encoding='utf-8') as archivo:
        try:
            pacientes_actuales = json.load(archivo)
        except json.JSONDecodeError:
            pacientes_actuales = []

# Imprimimos la tabla con los datos que existan
if len(pacientes_actuales) > 0:
    print(tabulate(pacientes_actuales, headers="keys", tablefmt="grid"))
else:
    print("La sala de espera está vacía.")