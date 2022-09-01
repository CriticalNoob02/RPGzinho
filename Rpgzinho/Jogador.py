import random
from Equipamentos import Equipamento, GerarEquipamento, Equipando

###################################################################### Classes Primárias:

class Personagem:
    def __init__(self):
        num = 1 ## Lógica de Balanceamento de atributos;
        self.vida = random.randint(5,7) 
        num += 7 - self.vida
        self.mana = random.randint(3,4) 
        num += 4 - self.mana
        self.força = random.randint(3,4) 
        num += 4 - self.força
        self.inteligencia = random.randint(2,4) 
        num += 4 - self.inteligencia
        self.energia = num

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

class Jogador(Raça, Classes,Equipamento):
    def __init__(self, Nome):
        super().__init__()
        self.nome = Nome
        self.raça = ""
        self.classe = ""
    def MontarPersonagem(self,raça,classe):
        self.raça = raça
        self.classe = classe
    def MostrarStatus(self):
        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raça}")
        print(f"Classe: {self.classe}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Vida: {self.vida}")
        print(f"Mana: {self.mana}")
        print(f"Força: {self.força}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Energia: {self.energia}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")

###################################################################### Criando Personagem;

def CriaçãoPersonagem():
    Nome = input("Digite o Nome do Seu Personagem: ")
    raça = input("Digite a Raça do Seu Personagem: ")
    classe = input("Digite a Classe do Seu Personagem: ")

    jogador01 = Jogador(Nome)

    if raça == "Humano":
        jogador01.Humano()
    elif raça == "Topeira":
        jogador01.Topeiras()
    elif raça == "Voador":
        jogador01.Voadores()
    elif raça == "Aquatico":
        jogador01.Aquaticos()
    elif raça == "Exosfera":
        jogador01.Exosferas()
    else:
        print("A Raça escolhida não existe!! ")

    if classe == "Medico":
        jogador01.Medico()
    elif classe == "Guerreiro":
        jogador01.Guerreiro()
    elif classe == "Mago":
        jogador01.Mago()
    elif classe == "Caçador":
        jogador01.Caçador()
    elif classe == "Tanque":
        jogador01.Tanque()
    
    jogador01.MontarPersonagem(raça, classe)
    jogador01.MostrarStatus()

    return jogador01


    d4 = random.randint(1,4)
    return d4

Jogador1 = CriaçãoPersonagem()
equipamento = GerarEquipamento()
print(equipamento)
Equipando(equipamento,Jogador1)

Jogador1.MostrarStatus()
Jogador1.MostrarEquipamento()