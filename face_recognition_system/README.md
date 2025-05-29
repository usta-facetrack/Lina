# Face Recognition System

Este proyecto implementa un sistema de reconocimiento facial para registrar asistencia de estudiantes.

## Enfoque

Se utiliza la librería InsightFace (ArcFace) para generar embeddings y comparar rostros. El sistema se mejora con:

- Preprocesamiento facial robusto (alineación, normalización)
- Umbral de distancia ajustable
- Manejo de errores y carpetas automáticas

## Estructura

- `main.py`: interfaz principal (CLI)
- `face_utils.py`: funciones de procesamiento y comparación
- `embeddings/`: embeddings guardados por usuario
- `fotos_usuarios/`: carpeta con fotos para registrar estudiantes
- `fotos_identificar/`: carpeta para identificar personas

## Uso

```bash
python main.py
```

1. Registrar: Colocar fotos en `./fotos_usuarios/NOMBRE` y seguir el menú.
2. Identificar: Colocar imagen en `./fotos_identificar/` y seguir el menú.

## Requisitos

```bash
pip install -r requirements.txt
```

