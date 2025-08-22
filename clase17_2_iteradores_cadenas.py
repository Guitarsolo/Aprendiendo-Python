# iterar en cadenas
text = 'Hola mundo'

# creando el objeto iterador
iter_text = iter(text)

# iterando en la cadena
for char in iter_text:
    print(char)

#for char in text: #aqui el resultado es el mismo, iter es mas eficiente en computo
    #print(char)
