to_do = ['Dirigirnos al hotel',
         'Ir a almorzar',
         'Visitar un museo',
         'Volver al hotel']
print(to_do)

numbers = [1,2,3,4,'cinco']
print(numbers)
print(type(numbers))

mix = ['uno', 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print('Primer elemento:',mix[0])
print('Segundo elemento:',mix[1])
print('Ultimo elemento:',mix[-1])

string = 'Hola mundo'
print(len(string))
print('Primer elemento:',string[0])
print('Segundo elemento:',string[1])
print('Ultimo elemento:',string[-1])

#Slice
print(mix[0:2])#devuelve desde el indice 0 hasta el indice 2-1
print(mix[2:5])
print(mix[:])#devuelve desde el primer al ultimo indice
print(mix[:2])#equivale al primer ejemplo

#agrega una lista a las listas
mix.append(False)#agrega una lista al final de la lista mix
print(mix)
mix.append(['a','b'])
print(mix)

#insertar
mix.insert(1,['a','b'])
print(mix)

#consultar indice de la aparicion de un primer elemento buscado en la lista
print(mix.index(['a','b']))

#
numbers = [1,2,100,90.45,3,4,5]
print(numbers)
print('Mayor:',max(numbers))
print('Menor:',min(numbers))

#eliminar elementos de la lista, inclusive la lista entera
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers #elimina toda la lista y en el codigo ya no existe
print(numbers)





