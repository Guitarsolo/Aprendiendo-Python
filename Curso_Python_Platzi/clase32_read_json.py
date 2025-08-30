import json #JSON (JavaScript Object Notation) es exactamente eso: una forma estandarizada y muy simple de escribir datos estructurados como texto. 

#Lectura del archivo
with open('products.json', 'r') as file:
    products = json.load(file)
    print(products)

#Recorrer el contenido
print('\n Recorrer el contenido:\n')
for product in products:
    #print(product)
    print(f'Producto: {product['name']}, Precio: {product['price']}')
