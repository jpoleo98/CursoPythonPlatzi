import random

def choise():
    opcionesTupla = (1,2,3)
    while True:
        player = input('1.Piedra - 2.Papel - 3.Tijera:');
        if player.isdigit():
            player = int(player)
            break
        else:
            print('introduzca una opcion valida')
            
    cpu = random.choice(opcionesTupla);
    
    return player, cpu

def checkRules(player,cpu,pwin,cpuwin,continuar):
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
        continuar = 'continue'
    
    return pwin,cpuwin,continuar

def checkwinner(pwin,cpuwin,turnosWins):
    if turnosWins == pwin:
        print('Ganador Player')
        return 'break'
        
    if turnosWins == cpuwin:
        print('Gano CPU')
        return 'break'


def main():
    pwin=0
    cpuwin=0
    turnos = 10
    i = 1   
    turnosWins=3
    continuar = ''

    while i<=turnos:
        print(f'Ronda {i} de {turnos}')

        player, cpu = choise()
        pwin, cpuwin, validadError = checkRules(player,cpu,pwin,cpuwin,continuar)
        if validadError == 'continue':
            continue
        
        ganador = checkwinner(pwin,cpuwin,turnosWins)

        if ganador == 'break':
            break

        i+=1

main()