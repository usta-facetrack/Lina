import os
import cv2
import numpy as np
import pickle
import unicodedata
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity

# Inicialización del modelo
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(640, 640))

def limpiar_nombre(nombre):
    nombre = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore').decode('utf-8')
    return nombre.replace(" ", "_").lower()

def obtener_embedding(path_img):
    img = cv2.imread(path_img)
    if img is None:
        print(f"⚠️ No se pudo leer la imagen: {path_img}")
        return None
    faces = app.get(img)
    if not faces:
        print(f"⚠️ No se detectaron rostros en la imagen: {path_img}")
        return None
    return faces[0].embedding

def registrar_persona(nombre, ruta_fotos, ruta_guardado):
    nombre_limpio = limpiar_nombre(nombre)
    os.makedirs(ruta_guardado, exist_ok=True)
    embeddings = []
    for archivo in os.listdir(ruta_fotos):
        path_img = os.path.join(ruta_fotos, archivo)
        emb = obtener_embedding(path_img)
        if emb is not None:
            embeddings.append(emb)
    if embeddings:
        with open(os.path.join(ruta_guardado, f"{nombre_limpio}.pkl"), "wb") as f:
            pickle.dump(np.array(embeddings), f)
        print(f"✅ {nombre} registrado con {len(embeddings)} imágenes.")
    else:
        print("⚠️ No se registraron embeddings válidos.")

def identificar_persona(path_img, ruta_embeddings, umbral=0.45):  # Ajuste del umbral aquí
    emb_consulta = obtener_embedding(path_img)
    if emb_consulta is None:
        return "Error de imagen"
    
    max_sim = -1
    nombre_identificado = "Desconocido"
    
    for archivo in os.listdir(ruta_embeddings):
        if archivo.endswith(".pkl"):
            with open(os.path.join(ruta_embeddings, archivo), "rb") as f:
                emb_guardado = pickle.load(f)
                sim = cosine_similarity([emb_consulta], emb_guardado).mean()
                print(f"🔍 Comparando con {archivo.replace('.pkl', '')}: similaridad = {sim:.4f}")  # NUEVO
    
                if sim > max_sim:
                    max_sim = sim
                    nombre_identificado = archivo.replace(".pkl", "").replace("_", " ").title()
    
    if max_sim >= 1 - umbral:
        return f"{nombre_identificado} (similaridad: {max_sim:.4f})"
    return f"Desconocido (similaridad: {max_sim:.4f})"

