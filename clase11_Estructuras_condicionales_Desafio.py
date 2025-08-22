# Reto: Hacer un piedra, papel o tijera. Debes evaluar la entrada de dos jugadores mediante la funcion input, luego usar las estructuras condicionales
# para devolver quien ha sido el ganador.
valid_moves = ['piedra','papel','tijera']

print('Bienvenido al juego piedra, papel o tijera!')

player_1_name = input('Jugador 1: ingresa tu nombre:')
player_2_name = input('Jugador 2: ingresa tu nombre:')

player_1_move = input(player_1_name + ' ingrese piedra, papel o tijera:')
if player_1_move not in valid_moves:
    print(player_1_name + ' elección incorrecta, seleccione una opción valida (piedra, papel o tijeras).')
player_2_move = input(player_2_name + ' ingrese piedra, papel o tijera:')
if player_2_move not in valid_moves:
    print(player_2_name + ' elección incorrecta, seleccione una opción valida (piedra, papel o tijeras).')

if player_1_move == player_2_move:
    print('Empate!')
elif player_1_move == 'piedra' and player_2_move == 'tijera' or \
     player_1_move == 'papel' and player_2_move == 'piedra' or \
     player_1_move == 'tijera' and player_2_move == 'papel':
     print(player_1_name + ' es el ganador!')
else :
    print(player_2_name + 'es el ganador!')
     




    
