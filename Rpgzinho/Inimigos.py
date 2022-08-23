import random

###################################################################### Classe Pai:

class Inimigos:
    def __init__(self):
        self.vida = 1 
        self.mana = 1 
        self.força = 1 
        self.inteligencia = 1
        self.energia = 1

###################################################################### Classes Filhos:

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