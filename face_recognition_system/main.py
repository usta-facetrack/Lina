import os
import re
from face_utils import registrar_persona, identificar_persona

def limpiar_nombre(nombre):
    # Elimina caracteres inválidos para nombres de carpetas en Windows
    nombre = re.sub(r"[^\w\s-]", "", nombre)  # quita puntos y símbolos raros
    nombre = nombre.strip()  # quita espacios extremos
    return nombre

def menu():
    print("\n[SISTEMA RECONOCIMIENTO FACIAL]")
    print("1. Registrar nueva persona")
    print("2. Identificar persona en imagen")
    print("3. Salir")
    return input("Seleccione una opción: ")

while True:
    opcion = menu()
    if opcion == "1":
        nombre = input("Nombre de la persona: ")
        nombre_limpio = limpiar_nombre(nombre)
        ruta_fotos = f"./fotos_usuarios/{nombre_limpio}"
        input(f"📂 Coloca las fotos en: {ruta_fotos} y presiona Enter para continuar...")
        registrar_persona(nombre, ruta_fotos, "./embeddings")
    elif opcion == "2":
        ruta_imagen = input("Ruta de la imagen a identificar: ")
        resultado = identificar_persona(ruta_imagen, "./embeddings")
        print(f"🧠 Persona identificada: {resultado}")
    elif opcion == "3":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida. Intente de nuevo.")
