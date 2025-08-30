#Leer un archivo linea por linea
"""with open('cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Grabar todas las lineas en una lista
"""with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#Agregar texto al final
"""with open('cuento.txt', 'a') as file:
    file.write("\n\nBy: DJM")"""

#Sobreescribir el texto
with open('cuento.txt', 'w') as file:
    file.write("\n\nBy: DJM")

#Conteo de lineas del texto
with open ("caperucita.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(len(lineas))