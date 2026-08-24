# Plan de Proyecto: Sistema de Triage y Priorización de Recepción Veterinaria

## 1. El Problema (Apartado de Negocio)
En las clínicas y hospitales veterinarios con alta demanda, los pacientes llegan simultáneamente a la sala de recepción. Actualmente, el personal administrativo (que no suele tener formación médica avanzada) atiende a los dueños por orden de llegada. Esto genera un cuello de botella peligroso donde mascotas en estado crítico pierden minutos vitales esperando su turno, mientras que pacientes estables acaparan la atención inicial. 

El objetivo de este proyecto es construir el motor lógico de un Módulo de Triage rápido. El programa actuará como un filtro automático en la recepción que evaluará dos signos vitales básicos e indicará inmediatamente al recepcionista en qué sala debe esperar el paciente (Box de Reanimación, Observación o Espera General), garantizando que los casos de riesgo vital pasen primero.

## 2. Los Datos y la Regla de Decisión (Apartado Técnico)
El programa procesará el ingreso de un paciente a la vez a través de la consola, capturando los datos mediante la función `input()` y convirtiéndolos a números enteros con `int()`. 

Se evaluarán dos variables clave:
1. `dificultad_respiratoria`: (1 = Sí tiene ahogo, 0 = No tiene ahogo).
2. `nivel_dolor`: Escala del 1 al 10.

Utilizando estructuras condicionales (`if` y `elif`), el algoritmo generará uno de los siguientes cuatro dictámenes:
* **Dato Inválido:** Si los datos ingresados no corresponden a las escalas permitidas (ej. dolor menor a 1 o mayor a 10).
* **Aceptado (Código Rojo):** Si hay dificultad respiratoria (1), el paciente ingresa de inmediato a Reanimación, independientemente de su nivel de dolor.
* **Rechazado para Urgencia Vital 1 (Código Amarillo):** Si no hay dificultad respiratoria (0), pero el dolor es alto (6 a 10). Se deriva a Observación para manejo del dolor.
* **Rechazado para Urgencia Vital 2 (Código Verde):** Si no hay dificultad respiratoria (0) y el dolor es bajo (1 a 5). Se deriva a la Sala de Espera General.

## 3. Priorización de Requerimientos (Modelo MoSCoW)

### Must Have (Debe tener obligatoriamente)
* Un script en Python (`solucion.py`) que solicite por consola la dificultad respiratoria y el nivel de dolor utilizando `int()`.
* Una estructura condicional `if/elif` que procese las dos variables y retorne las cuatro salidas estipuladas.
* Almacenamiento de cada registro de triage como un diccionario dentro de un archivo local llamado `datos.json` utilizando la librería `json`.

### Should Have (Debería tener)
* Manejo básico de errores para notificar al usuario si ingresa un rango de dolor inválido.
* Uso de la librería `tabulate` para mostrar un resumen claro por consola de los pacientes que ya han sido ingresados en la jornada.

### Could Have (Podría tener)
* Una vista de lectura web construida con Django (`views.py`) que consuma el archivo `datos.json` y envíe la información a un template (`resumen.html`) para visualizar un panel de control con el estado de la sala de espera.

### Won't Have (No tendrá por ahora)
* Conexión a bases de datos relacionales o no relacionales.
* Diagnósticos médicos detallados de la mascota o prescripción de medicamentos.
* Cuenta de usuarios.