import os

#Obtener el directorio actual
cwd = os.getcwd()
print('Directorio de trabajo actual:', cwd)

#Listar los archivos
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Los archivos txt son:', txt_files)

#Renombrar un archivo
os.rename('cuento.txt','Çaperucita.txt')
print('Nombre modificado')
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Los archivos txt son:', txt_files)
