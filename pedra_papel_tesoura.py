from random import randint
from time import sleep
 
def calculo():
    if computador == 1:
        if jogador == 1: # Pedra - pedra
            print('EMPATE')
    
        elif jogador == 2:
            print('JOGADOR VENCEU!') #pedra - papel

        elif jogador == 3:
            print('COMPUTADOR VENCEU!') #PEDRA - tesoura

        else:
            print('JOGADA INVALIDA')

    if computador == 2:
        if jogador == 1: #papel - pedra
            print('COMPUTADOR VENCEU')

        elif jogador == 2: # papel = papel
            print('EMPATE')

        elif jogador == 3: # papel - tesoura
            print('JOGADOR VENCEU')

        else: 
            print('JOGADA INVALIDA')

    if computador == 3: 
        if jogador == 1: # tesoura - pedra
            print('JOGADOR VENCEU')

        elif jogador == 2: # tesoura - papel
            print('COMPUTADOR VENCEU')

        elif jogador == 3: # tesoura - tesoura
            print('EMPATE')
        
        else:
            print('JOGADA INVALIDA')



itens =['' , 'pedra', 'papel', 'tesoura']
computador = randint(1, 3)

print('''escolha a opção: 
    [1] pedra
    [2] papel
    [3] tesoura''')
jogador = int(input('Me informe sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
print('-' * 11)

print(f'o computador jogou: {itens[computador]}')
print(f'você jogou: {itens[jogador]}')
print('-' * 11)

# Mostra os resultados 

if computador == 1:
    if jogador == 1: # Pedra - pedra
        print('EMPATE')
    
    elif jogador == 2:
        print('JOGADOR VENCEU!') #pedra - papel

    elif jogador == 3:
        print('COMPUTADOR VENCEU!') #PEDRA - tesoura

    else:
        print('JOGADA INVALIDA')

if computador == 2:
    if jogador == 1: #papel - pedra
        print('COMPUTADOR VENCEU')

elif jogador == 2: # papel = papel
    print('EMPATE')

elif jogador == 3: # papel - tesoura
        print('JOGADOR VENCEU')

else: 
    print('JOGADA INVALIDA')

if computador == 3: 
    if jogador == 1: # tesoura - pedra
        print('JOGADOR VENCEU')

    elif jogador == 2: # tesoura - papel
        print('COMPUTADOR VENCEU')

    elif jogador == 3: # tesoura - tesoura
        print('EMPATE')
        
    else:
        print('JOGADA INVALIDA')