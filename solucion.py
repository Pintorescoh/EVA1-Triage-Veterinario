import json
import os
from tabulate import tabulate

# 1. Solicitar datos al usuario
nombre_mascota = input("Nombre paciente: ")
dificultad_respiratoria = int(input("¿Tiene ahogo o dificultad para respirar? (1=Sí, 0=No): "))
nivel_dolor = int(input("Nivel de dolor aparente (1 al 10): "))

resultado = ""

# 2. Motor de decisiones (Los 4 resultados)
if dificultad_respiratoria not in [0, 1] or nivel_dolor < 1 or nivel_dolor > 10:
    resultado = "Inválido"
    print("Error: Los datos de evaluación ingresados son inválidos.")

elif dificultad_respiratoria == 1:
    resultado = "Código Rojo"
    print(f"Aceptado: Pase directo de Urgencia. {nombre_mascota} entra a Sala de Reanimación (Código Rojo).")

elif dificultad_respiratoria == 0 and nivel_dolor >= 6:
    resultado = "Código Amarillo"
    print(f"Rechazado 1 (Sin Urgencia Vital): {nombre_mascota} respira bien pero tiene dolor agudo. Pasa a Sala de Atención (Código Amarillo).")

elif dificultad_respiratoria == 0 and nivel_dolor < 6:
    resultado = "Código Verde"
    print(f"Rechazado 2 (Estable): {nombre_mascota} está estable. Pasa a Sala de Espera General (Código Verde).")

# 3. Empaquetar y guardar (Solo si el dato es válido)
if resultado != "Inválido":
    
    if dificultad_respiratoria == 1:
        texto_respiracion = "Sí"
    else:
        texto_respiracion = "No"

    nuevo_paciente = {
        "Nombre": nombre_mascota,
        "Dificultad_Respiracion": texto_respiracion,
        "Dolor": nivel_dolor,
        "Gravedad": resultado
    }

    archivo_json = "datos.json"

    # Revisar si existe el historial viejo
    if os.path.exists(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo_viejo:
            lista_pacientes = json.load(archivo_viejo)
    else:
        lista_pacientes = []

    # Agregar el nuevo paciente y sobreescribir el archivo
    lista_pacientes.append(nuevo_paciente)

    with open(archivo_json, "w", encoding="utf-8") as archivo_nuevo:
        json.dump(lista_pacientes, archivo_nuevo, indent=4, ensure_ascii=False)
    
    print("\n[+] ¡Registro guardado exitosamente en el sistema!\n")
    
    # 4. Dibujar la tabla
    print("--- ESTADO ACTUAL DE LA SALA ---")
    tabla_dibujada = tabulate(lista_pacientes, headers="keys", tablefmt="grid")
    print(tabla_dibujada)