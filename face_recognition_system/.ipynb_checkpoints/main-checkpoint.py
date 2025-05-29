
import os
from face_utils import registrar_persona, identificar_persona

menu = """
[SISTEMA RECONOCIMIENTO FACIAL]
1. Registrar nueva persona
2. Identificar persona en imagen
3. Salir
"""

while True:
    print(menu)
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Nombre de la persona: ")
        ruta_fotos = "./fotos_usuarios/" + nombre
        os.makedirs(ruta_fotos, exist_ok=True)
        print(f"Coloca las fotos en: {ruta_fotos} y presiona Enter...")
        input()
        registrar_persona(nombre, ruta_fotos, "./embeddings")
    elif opcion == "2":
        ruta_imagen = input("Ruta de la imagen a identificar: ")
        resultado = identificar_persona(ruta_imagen, "./embeddings")
        print(resultado)
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
