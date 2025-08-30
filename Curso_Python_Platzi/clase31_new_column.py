import csv

file_path = 'products.csv'
updated_file_path = 'products_updated.csv'

with open(file_path, mode = 'r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    field_names = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode = 'w', newline = '') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames = field_names) #  Es como contratar a un escriba ✍️. Le das sus instrucciones iniciales: en qué archivo debe escribir (updated_file) y qué columnas debe usar (fieldnames). En este punto, aún no ha escrito nada, solo sabe cuáles son las reglas.
        csv_writer.writeheader() #Le dices: "Ahora, escribe la fila de encabezados que te di en las instrucciones". Esto crea la primera línea del nuevo archivo CSV con los nombres de todas las columnas, incluyendo la nueva 'total_value'.

        for row in csv_reader: # Por cada fila del archivo original, el código calcula el total_value y la agrega al diccionario row. Luego, le das la orden al escriba: "Toma este diccionario row completo y escríbelo como una nueva fila". Esto se repite hasta que se han procesado todas las filas del archivo original.
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)

