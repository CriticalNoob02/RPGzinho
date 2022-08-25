import random
from Gerar_Nomes import Nome

###################################################################### Classe Pai (Base do Inimigo);

class Inimigos:
    def __init__(self):
        self.vida =  1
        self.mana = 1 
        self.força = 1 
        self.inteligencia = 1
        self.energia = 1

###################################################################### Classes Filhos (Classes e Raças dos Inimigos);

class IniRaça(Inimigos):
    def __init__(self):
        super().__init__()
    
    def IniHumano(self, Nivel):
        Nivel += 2
        self.vida +=  random.randint(0,Nivel)
        self.mana += random.randint(0,Nivel)
        self.força += random.randint(0,Nivel)
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

    def IniGoblin(self, Nivel):
        Nivel += 3
        self.vida += 1
        self.mana += 1
        self.força += random.randint(0,Nivel)
        self.inteligencia += 1
        self.energia += random.randint(0,Nivel)

    def IniTopeira(self, Nivel):
        Nivel += 4
        self.vida +=  random.randint(0,Nivel)
        self.mana += 1
        self.força += random.randint(0,Nivel)
        self.inteligencia += 0
        self.energia += random.randint(0,Nivel) 

    def IniGolem(self, Nivel):
        Nivel += 4
        self.vida +=  random.randint(0,Nivel)
        self.mana += random.randint(0,Nivel)
        self.força += random.randint(0,Nivel)
        self.inteligencia += 0
        self.energia += 1

    def IniVoador(self, Nivel):
        Nivel += 3
        self.vida +=  3
        self.mana += 1
        self.força += random.randint(0,Nivel)
        self.inteligencia += 0
        self.energia += random.randint(0,Nivel)

    def IniAquatico(self, Nivel):
        Nivel += 3
        self.vida += random.randint(0,Nivel)
        self.mana += 1
        self.força += random.randint(0,Nivel)
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

    def IniAbyssais(self, Nivel):
        Nivel += 4
        self.vida += 2
        self.mana += random.randint(0,Nivel)
        self.força += 1
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

    def IniExosferas(self, Nivel):
        Nivel += 5
        self.vida += 0
        self.mana += random.randint(0,Nivel)
        self.força += 0
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

class IniClasses(Inimigos):
    def __init__(self):
        super().__init__()

    def IniMedico(self, Nivel):
        Nivel += 3
        self.vida +=  random.randint(0,Nivel)
        self.mana += 1
        self.força += 1
        self.inteligencia += random.randint(0,Nivel)
        self.energia += 1

    def IniLadrao(self, Nivel):
        Nivel += 5
        self.vida += 1
        self.mana += 1
        self.força += 1
        self.inteligencia += 1
        self.energia += random.randint(0,Nivel)

    def IniConstrutor(self, Nivel):
        Nivel += 3
        self.vida += 1
        self.mana += 0
        self.força += 0
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

    def IniGuerreiro(self, Nivel):
        Nivel += 3
        self.vida += random.randint(0,Nivel)
        self.mana += 0
        self.força += random.randint(0,Nivel)
        self.inteligencia += 1
        self.energia += random.randint(0,Nivel)

    def IniBruxo(self, Nivel):
        Nivel += 3
        self.vida += random.randint(0,Nivel)
        self.mana += random.randint(0,Nivel)
        self.força += 0
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

    def IniMago(self, Nivel):
        Nivel += 4
        self.vida += 1
        self.mana += random.randint(0,Nivel)
        self.força += 1
        self.inteligencia += random.randint(0,Nivel)
        self.energia += random.randint(0,Nivel)

    def IniCaçador(self, Nivel):
        Nivel += 3
        self.vida += random.randint(0,Nivel)
        self.mana += 0
        self.força += random.randint(0,Nivel)
        self.inteligencia += 2
        self.energia += random.randint(0,Nivel)

###################################################################### Classes Netas (Montagem do Inimigo);

class Inimigo(IniRaça, IniClasses):
    def __init__(self, Nivel, Nome):
        super().__init__()
        self.nivel = Nivel
        self.nome = Nome
        self.raça = ""
        self.classe = ""
    def MontarInimigo(self, Raça, Classe):
        self.raça = Raça
        self.classe = Classe
    def MostrarInimigo(self):
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

###################################################################### Classes Netas (Montagem do Inimigo);

def CriaçãoInimigo():
    nome = Nome()
    raça = random.randint(1,8)
    classe = random.randint(1,7)
    nivel = 1 ## Automatizar o Nivel dependendo da faseda História;

    inimigo1 = Inimigo(nivel, nome)

    match raça:
        case 1:
            inimigo1.IniHumano(nivel)
            raça = "Humano"
        case 2:
            inimigo1.IniGoblin(nivel)
            raça = "Goblin"
        case 3:
            inimigo1.IniTopeira(nivel)
            raça = "Topeira"
        case 4:
            inimigo1.IniGolem(nivel)
            raça = "Golem"
        case 5:
            inimigo1.IniVoador(nivel)
            raça = "Voador"
        case 6:
            inimigo1.IniAquatico(nivel)
            raça = "Aquatico"
        case 7:
            inimigo1.IniAbyssais(nivel)
            raça = "Abyssal"
        case 8:
            inimigo1.IniExosferas(nivel)
            raça = "Exosfera"
        
    match classe:
        case 1:
            inimigo1.IniMedico(nivel)
            classe = "Médico"
        case 2:
            inimigo1.IniLadrao(nivel)
            classe = "Ladrão"
        case 3:
            inimigo1.IniConstrutor(nivel)
            classe = "Construtor"
        case 4:
            inimigo1.IniGuerreiro(nivel)
            classe = "Guerreiro"
        case 5:
            inimigo1.IniBruxo(nivel)
            classe = "Bruxo"
        case 6:
            inimigo1.IniMago(nivel)
            classe = "Mago"
        case 7:
            inimigo1.IniCaçador(nivel)
            classe = "Caçador"

    inimigo1.MontarInimigo(raça, classe)
    inimigo1.MostrarInimigo()






    # def IniMostroMarinho(self, Nivel):
    #     Nivel += 5
    #     self.vida += random.randint(0,Nivel)
    #     self.mana += 1
    #     self.força += random.randint(0,Nivel)
    #     self.inteligencia += 0
    #     self.energia += 1

    # def IniLagarto(self, Nivel):
    #     Nivel += 2
    #     self.vida +=  random.randint(0,Nivel)
    #     self.mana += 1
    #     self.força += random.randint(0,Nivel)
    #     self.inteligencia += 0
    #     self.energia += random.randint(0,Nivel)

    # def IniPassaro(self, Nivel):
    #     Nivel += 2
    #     self.vida += 3
    #     self.mana += 1
    #     self.força += random.randint(0,Nivel)
    #     self.inteligencia += 0
    #     self.energia += random.randint(0,Nivel)

    # def IniPiranha(self, Nivel):
    #     Nivel += 2
    #     self.vida +=  1
    #     self.mana += 0
    #     self.força += random.randint(0,Nivel)
    #     self.inteligencia += 0
    #     self.energia += random.randint(0,Nivel)