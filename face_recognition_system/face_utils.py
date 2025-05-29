
import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from scipy.spatial.distance import cosine
import pickle

# Configurar modelo
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(640, 640))

def obtener_embedding(path_img):
    img = cv2.imread(path_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = app.get(img)
    if len(faces) != 1:
        print(f"❌ {os.path.basename(path_img)}: se detectaron {len(faces)} caras.")
        return None
    return faces[0].embedding

def registrar_persona(nombre, ruta_imagenes, ruta_guardado):
    embeddings = []
    for archivo in os.listdir(ruta_imagenes):
        if archivo.lower().endswith(('jpg', 'jpeg', 'png')):
            path_img = os.path.join(ruta_imagenes, archivo)
            emb = obtener_embedding(path_img)
            if emb is not None:
                embeddings.append(emb)
    if embeddings:
        with open(os.path.join(ruta_guardado, f"{nombre}.pkl"), "wb") as f:
            pickle.dump(embeddings, f)
        print(f"✅ {nombre} registrado con {len(embeddings)} imágenes.")

def identificar_persona(path_img, ruta_embeddings):
    emb_consulta = obtener_embedding(path_img)
    if emb_consulta is None:
        return "❌ No se pudo procesar la imagen."
    mejor_distancia = 1.0
    nombre_identificado = "Desconocido"
    for archivo in os.listdir(ruta_embeddings):
        if archivo.endswith(".pkl"):
            nombre = archivo.replace(".pkl", "")
            with open(os.path.join(ruta_embeddings, archivo), "rb") as f:
                embeddings = pickle.load(f)
            for emb in embeddings:
                dist = cosine(emb, emb_consulta)
                if dist < mejor_distancia:
                    mejor_distancia = dist
                    nombre_identificado = nombre
    return f"🧠 Persona identificada: {nombre_identificado} (distancia: {mejor_distancia:.4f})"
