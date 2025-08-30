import csv

#Leer un archivo
"""with open('products.csv', mode='r') as file:
    csv_dictreader = csv.DictReader(file)
    for row in csv_dictreader:
        print(row)"""
#Mostrar la informacion en columnas
with open('products.csv', mode='r') as file:
    csv_dictreader = csv.DictReader(file)
    print(csv_dictreader)
    for row in csv_dictreader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")