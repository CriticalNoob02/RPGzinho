import random

###################################################################### Classes Primárias:

class Personagem:
    def __init__(self):
        self.vida = random.randint(range(8,10))
        self.mana = random.randint(range(10,15))
        self.força = random.randint(range(10,15))
        self.inteligencia = random.randint(range(10,15))
        self.energia = random.randint(range(25,30))

###################################################################### Classes Secundária;

class Raça(Personagem):
    def __init__(self):
        super().__init__()

    def Humano(self):
        self.vida += 5
        self.mana += 5
        self.força += 5
        self.inteligencia += 5
        self.energia += 5

    def Topeiras(self):
        self.vida += 5
        self.mana += 0
        self.força += 15
        self.inteligencia += 0
        self.energia += 5

    def Voadores(self):
        self.vida += 5
        self.mana += 0
        self.força += 8
        self.inteligencia += 2
        self.energia += 10

    def Aquaticos(self):
        self.vida += 15
        self.mana += 0
        self.força += 0
        self.inteligencia += 0
        self.energia += 10

    def Exosferas(self):
        self.vida += 0
        self.mana += 10
        self.força += 0
        self.inteligencia += 15
        self.energia += 0

class Classes(Personagem):
    def __init__(self):
        super().__init__()

    def Medico(self):
        self.vida += 0
        self.mana += 5
        self.força += 0
        self.inteligencia += 5
        self.energia += 5

    def Guerreiro(self):
        self.vida += 5
        self.mana += 0
        self.força += 10
        self.inteligencia += 0
        self.energia += 0

    def Mago(self):
        self.vida += 0
        self.mana += 7
        self.força += 0
        self.inteligencia += 8
        self.energia += 0

    def Caçador(self):
        self.vida += 2
        self.mana += 0
        self.força += 2
        self.inteligencia += 1
        self.energia += 10

    def Tanque(self):
        self.vida += 12
        self.mana += 0
        self.força += 3
        self.inteligencia += 0
        self.energia += 0
    
###################################################################### Classes Netas;

class Jogador(Raça, Classes):
    def __init__(self, Nome):
        super().__init__()
        self.nome = Nome

def CriaçãoPersonagem():
    Nome = input("Digite o Nome do Seu Personagem: ")
    raça = input("Digite a Raça do Seu Personagem: ")
    classe = input("Digite a Classe do Seu Personagem: ")

    jogador01 = Jogador(Nome)

    if raça == 1:
        jogador01.Humano()
    elif raça == 2:
        jogador01.Topeiras()
    elif raça == 3:
        jogador01.Voadores()
    elif raça == 4:
        jogador01.Aquaticos()
    elif raça == 5:
        jogador01.Exosferas()
    else:
        print("A Raça escolhida não existe!! ")

    if classe == 1:
        jogador01.Medico()
    elif classe == 2:
        jogador01.Guerreiro()
    elif classe == 3:
        jogador01.Mago()
    elif classe == 4:
        jogador01.Caçador()
    elif classe == 5:
        jogador01.Tanque()