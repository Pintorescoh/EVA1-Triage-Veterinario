# 🏥 Sistema de Triage y Priorización de Recepción Veterinaria

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

Este proyecto es una solución híbrida (Consola + Web) diseñada para automatizar y priorizar el ingreso de pacientes en clínicas veterinarias con alta demanda. Mediante un motor de evaluación de dos variables (dificultad respiratoria y nivel de dolor), el sistema emite un código de gravedad y deriva al paciente a la sala correspondiente.

> **Nota para evaluación:** Las justificaciones de negocio, la lógica de decisión técnica y la priorización de requerimientos (MoSCoW) se encuentran detalladas en el archivo [`plan.md`](./plan.md) adjunto en este repositorio.

---

## 🚀 Características Principales (Fases del Proyecto)

1. **Ingreso por Consola:** Script de Python (`solucion.py`) que captura y valida datos sanitarios mediante ingresos controlados (`input()` y conversión a `int()`).
2. **Motor de Decisiones:** Lógica condicional (`if/elif`) que clasifica a los pacientes en tres códigos: Rojo (Reanimación), Amarillo (Observación) y Verde (Espera General).
3. **Persistencia de Datos:** Almacenamiento automático y seguro del historial de ingresos en formato `datos.json`.
4. **Visualización en Terminal:** Uso de la librería `tabulate` para generar un resumen tabular inmediato para el recepcionista.
5. **Dashboard Web:** Integración con **Django** para consumir el archivo JSON y desplegar una pantalla de monitoreo con indicadores de color dinámicos basados en la gravedad.

---

## 📂 Estructura del Proyecto
solucion.py: Motor lógico principal de captura, evaluación de triage y escritura.

datos.json: Base de datos documental que almacena los ingresos del día.

plan.md: Documento de planificación y reglas de negocio.

manage.py & /clinica/: Archivos de configuración principal del servidor Django.

/recepcion/: App de Django encargada de la vista de la sala de espera.

/recepcion/views.py: Cerebro que lee el JSON y envía el contexto.

/recepcion/templates/recepcion/sala.html: Plantilla de diseño del monitor web.

## 🛠️ Instalación y Uso

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Pintorescoh/ES1-Sistema-de-Triage-Veterinario-con-Django-.git](https://github.com/Pintorescoh/ES1-Sistema-de-Triage-Veterinario-con-Django-.git)
cd ES1-Sistema-de-Triage-Veterinario-con-Django
2. Instalar dependencias
Asegúrate de tener instalado Python y ejecuta en tu terminal:

```bash
pip install tabulate django
3. Ejecutar el motor de Consola (Backend)
Para ingresar nuevos pacientes a la sala de espera, ejecuta el script principal:

```bash
python solucion.py
(Sigue las instrucciones en pantalla para evaluar a la mascota. Los datos se guardarán automáticamente en datos.json).

4. Iniciar el Dashboard Web (Frontend)
Para visualizar el estado de la sala en tiempo real, levanta el servidor de Django:

```Bash
python manage.py runserver
Luego, abre tu navegador y visita: http://127.0.0.1:8000/