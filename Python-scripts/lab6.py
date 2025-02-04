import os

# Definir la ruta donde se creará el archivo
ruta_directorio = "C:\\Users\\jinch\\Desktop"
nombre_archivo = "mi_archivo.txt"
ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

# Mensaje que se escribirá en el archivo
mensaje = "¡Hola, este es un archivo creado con Python!"

# Crear y escribir en el archivo
try:
    with open(ruta_completa, 'w') as archivo:
        archivo.write(mensaje)
    print(f"Archivo creado exitosamente en: {ruta_completa}")
except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")