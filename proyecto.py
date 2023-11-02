import random

player = int(input('1.Piedra - 2.Papel - 3.Tijera:'));
cpu = random.randint(1,3);

if player >= 1 and player<=3:
    if player==cpu:
        print('Empate')
    elif (player==1 and cpu==3) or (player==2 and cpu==1)  or (player==3 and cpu==2):
        print('Player Ganador')
    else:
        print('CPU Ganador');
else:
    print('introduzca una opcion valida')