# Face Recognition System – Registro de Asistencia

Este proyecto implementa y mejora un sistema de reconocimiento facial para registrar la asistencia de estudiantes en entornos reales, combinando la librería InsightFace (ArcFace) con un flujo robusto de preprocesamiento y comparación de rostros.

---

## Objetivo

Diseñar mejoras al pipeline de reconocimiento facial enfocado en aumentar la precisión y robustez bajo condiciones reales. No se requiere interfaz gráfica ni despliegue web.

---

## Enfoque y mejoras implementadas

- Se reemplazó FaceNet por **ArcFace (InsightFace)** para una mayor precisión en embeddings.
- Se integró preprocesamiento robusto: detección, alineación y normalización de rostros.
- Se ajustó el umbral de similitud con validación manual.
- Se automatizó la creación de carpetas, manejo de errores y limpieza de datos inválidos.

---

## Estructura del Proyecto

```
face_recognition_system/
├── main.py                     # Interfaz principal (menú CLI)
├── face_utils.py               # Registro e identificación de personas
├── embeddings/                 # Embeddings faciales (.pkl por persona)
├── fotos_usuarios/             # Fotos de entrenamiento por persona
├── fotos_identificar/          # Imagen a identificar
├── requirements.txt            # Dependencias del entorno
├── README.md                   # Instrucciones y documentación
```

---

## Uso del sistema

1. **Instalar las dependencias:**

```bash
pip install -r requirements.txt
```

2. **Ejecutar el programa:**

```bash
python main.py
```

3. **Registrar un estudiante:**

- El sistema te pedirá un nombre.
- Crea automáticamente la carpeta `./fotos_usuarios/NOMBRE`.
- Coloca al menos 3-5 imágenes claras del rostro en dicha carpeta.
- Presiona Enter para continuar y registrar los embeddings.

4. **Identificar una persona:**

- Coloca la imagen en `./fotos_identificar/`.
- Ingresa la ruta completa cuando el sistema lo pida.
- El sistema devuelve el nombre de la persona más similar o "Desconocido".

---

## Resultados

- Evaluaciones muestran reconocimiento robusto incluso con expresiones o fondos variados.
- Similaridades por encima de 0.6 se consideran aceptables para identificación positiva.

---

## Consideraciones éticas

- El sistema no recolecta datos automáticamente.
- El uso está restringido a propósitos académicos y educativos.
- Se promueve el consentimiento informado y respeto a la privacidad.

---

## Créditos

Desarrollado como parte del curso de Redes Neuronales – Universidad Santo Tomás  
Autor: [Lina Alejandra Fierro Porras]



