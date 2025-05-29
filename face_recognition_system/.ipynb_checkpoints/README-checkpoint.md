# Sistema de Reconocimiento Facial

Este proyecto permite registrar rostros junto con nombres y luego identificar personas usando ArcFace e InsightFace.

## Requisitos
```bash
pip install -r requirements.txt
```

## Uso
```bash
python main.py
```

## Funcionalidades
- Registrar persona: nombre + imágenes.
- Guardar embeddings alineados por persona.
- Identificar persona en una nueva imagen.

Los embeddings se guardan en `embeddings/` y las imágenes cargadas en `fotos_usuarios/`.

## Créditos
- Basado en ArcFace/InsightFace con modelos preentrenados `buffalo_l`.
