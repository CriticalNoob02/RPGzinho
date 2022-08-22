from configparser import RawConfigParser
import random

## Classes Primárias:
class Personagem:
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        self.vida = Vida
        self.mana = Mana
        self.força = Força
        self.inteligencia = Inteligencia
        self.energia = Energia
    def gerarAtributos(self):
        self.vida = random.randint(range(8,10))
        self.mana = random.randint(range(10,15))
        self.força = random.randint(range(10,15))
        self.inteligencia = random.randint(range(10,15))
        self.energia = random.randint(range(25,30))

## Classes Secundária;
class Humano(Personagem):
    def __init__(self, Vida , Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 5
        self.mana += 5
        self.força += 5
        self.inteligencia += 5
        self.energia += 5

class Topeiras(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 5
        self.mana += 0
        self.força += 15
        self.inteligencia += 0
        self.energia += 5

class Voadores(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 5
        self.mana += 0
        self.força += 8
        self.inteligencia += 2
        self.energia += 10

class Aquaticos(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 15
        self.mana += 0
        self.força += 0
        self.inteligencia += 0
        self.energia += 10

class Exosferas(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 0
        self.mana += 10
        self.força += 0
        self.inteligencia += 15
        self.energia += 0

## Classes de Ocupação;
class Medico(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 0
        self.mana += 5
        self.força += 0
        self.inteligencia += 5
        self.energia += 5

class Guerreiro(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 5
        self.mana += 0
        self.força += 10
        self.inteligencia += 0
        self.energia += 0

class Mago(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 0
        self.mana += 7
        self.força += 0
        self.inteligencia += 8
        self.energia += 0

class Caçador(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 2
        self.mana += 0
        self.força += 2
        self.inteligencia += 1
        self.energia += 10
    
class Tanque(Personagem):
    def __init__(self, Vida, Mana, Força, Inteligencia, Energia):
        super().__init__(Vida, Mana, Força, Inteligencia, Energia)
        self.vida += 12
        self.mana += 0
        self.força += 3
        self.inteligencia += 0
        self.energia += 0

## Criando Jogador;
