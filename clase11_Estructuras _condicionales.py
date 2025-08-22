#IF
x=5
if x>5:
    print('x es mayor que 5')# python es estrictamente identado
elif x==5: # es un else if, se usa para verificar condiciones adicionales una vez que el if inicial sea falso,se pueden usar la cantidad que sean necesarios
    print('x es igual a 5')
else:
    print('x es menor que 5')
print('Afuera del if')

# AND y OR
a=15
b=26

if a > 10 and b > 25: # ambas condiciones deben ser verdaderas
    print('A es mayor a 10 y Y es mayor a 25')
if a > 10 or b > 25: # al menos una de las condiciones deben ser verdaderas
    print('A es mayor a 10 o Y es mayor a 25')
# NOT
z = 11
if not z > 10:
    print('Z no es mayor que 10')
else:
    print('Z es mayor que 10')


# IFs anidados
is_member = True
age = 15
if is_member == True:
    if age >= 15:
        print('Tienes acceso ya que eres miembro y tu edad es mayor o igual a 15 años')
    else:
        print('No tienes acceso, ya que eres miembro pero tu edad es menor a 15 años')
else:
    print('No tienes acceso, no eres miembro')



