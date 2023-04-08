# teste de criar classe
class Carro:
    def __init__(self, marca, motor, versão):
        self.marca = marca
        self.motor = motor
        self.versão = versão

    def Ligar(self):
        while True:
            resposta = input('Você gostaria de ligar o Carro [s/n]?: ')
            if resposta != 's':
                print('então isso é apenas um carro desligado!')
            else:
                print('ESTOU LIGANDO! VRUMMM')
                break
        
    def especificações(self):
        while True:
            resposta2 = input('Gostaria de ver as especificações [s/n]?: ')
            if resposta2 == 's':
                print(f'eu sou um {self.marca}, do motor {self.motor} e sou da versão {self.versão}')
                break
            else:
                print('Então oque você quer porra? sou simples merda!')
    def desligar(self):
        resposta3 = input('Você gostaria de desligar o carro agora [s/n]?: ')
        while True:
            if resposta3 == 's':
                print('o carro desligou')
                break
            else:
                print('O carro morreu!')
                break

Gol = Carro('Gol', '100', '2008')
Gol.Ligar()
Gol.especificações()
Gol.desligar()
