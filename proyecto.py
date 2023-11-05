import random

opcionesTupla = (1,2,3)

turnos = 10
i = 1
pwin=0
cpuwin=0

turnosWins=3

while i<=turnos:
    print(f'Ronda {i} de {turnos}')
    while True:
        player = input('1.Piedra - 2.Papel - 3.Tijera:');
        if player.isdigit():
            player = int(player)
            break
        else:
            print('introduzca una opcion valida')
            
    cpu = random.choice(opcionesTupla);

    if player >= 1 and player<=3:
        if player==cpu:
            print('Empate')
        elif (player==1 and cpu==3) or (player==2 and cpu==1)  or (player==3 and cpu==2):
            print('Player Ganador')
            pwin+=1
        else:
            print('CPU Ganador');
            cpuwin+=1
    else:
        print('introduzca una opcion valida')
        continue

    if turnosWins == pwin:
        print('Ganador Player')
        break
    
    if turnosWins == cpuwin:
        print('Gano CPU')
        break
    i+=1
