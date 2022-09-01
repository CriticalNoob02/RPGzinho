###################################################################### Classes Primárias:

import random


class Cabeça():
    def __init__(self) -> None:
        pass
    
    def Capacete(self):
        self.vida += 10
        self.mana += 0
        self.força += 3 
        self.inteligencia += 0
        self.energia -= 2

    def Gorro(self):
        self.vida -= 2
        self.mana += 10
        self.força += 0 
        self.inteligencia += 3
        self.energia += 0
    
    def Capuz(self):
        self.vida += 0
        self.mana += 0
        self.força += 1
        self.inteligencia += 0
        self.energia += 10
       
class CorpoSuperior():
    def __init__(self) -> None:
        pass

    def PeitoralFerro(self):
        self.vida += 15
        self.mana += 0
        self.força += 0 
        self.inteligencia += 0
        self.energia -= 2

    def VestidoMagico(self):
        self.vida -= 2
        self.mana += 12
        self.força += 0 
        self.inteligencia += 3
        self.energia += 0

    def RoupaCamuflada(self):
        self.vida += 0
        self.mana += 0
        self.força += 2
        self.inteligencia += 0
        self.energia += 13

class CorpoInferior():
    def __init__(self) -> None:
        pass

    def CalçaFerro(self):
        self.vida += 7
        self.mana += 0
        self.força += 0
        self.inteligencia += 0
        self.energia += 0

    def CuecaEstrelada(self):
        self.vida += 0
        self.mana += 5
        self.força += 0 
        self.inteligencia += 2
        self.energia -= 0

    def CalçaLegging(self):
        self.vida += 0
        self.mana += 0
        self.força += 1 
        self.inteligencia += 0
        self.energia += 6

class Arma():
    def __init__(self) -> None:
        pass

    def Espadão(self):
        self.vida += 0
        self.mana += 0
        self.força += 11 
        self.inteligencia += 0
        self.energia -= 0

    def VaraDeMoises(self):
        self.vida += 0
        self.mana += 0
        self.força += 0 
        self.inteligencia += 11
        self.energia += 0

    def ArcoLongo(self):
        self.vida += 0
        self.mana += 0
        self.força += 5 
        self.inteligencia += 0
        self.energia -= 6

class Equipamento(Cabeça,CorpoSuperior,CorpoInferior,Arma):
    def __init__(self) -> None:
        super().__init__()
        self.cabeça = "Nada"
        self.corpoSuperior = "Nada"
        self.corpoInferior = "Nada"
        self.arma = "Nada"

    def AdicionandoEquipamento(self,num,nome):
        match num:
            case 1:
                self.cabeça = nome
            case 2:
                self.corpoSuperior = nome
            case 3:
                self.corpoInferior = nome
            case 4:
                self.arma = nome
        
    
    def MostrarEquipamento(self):
        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Cabeça: {self.cabeça}")
        print(f"Corpo Superior: {self.corpoSuperior}")
        print(f"Corpo Inferior: {self.corpoInferior}")
        print(f"Arma: {self.arma}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")

## Gerando Equipamento Aleatório;
def GerarEquipamento():
    local = random.randint(1,4)
    match local:
        case 1:
            equipamento = random.choices(["Capacete","Gorro","Capuz"]) 
        case 2:
            equipamento = random.choices(["Peitoral de Ferro","Vestido Mágico","Roupa Camulfada"])
        case 3:
            equipamento = random.choices(["Calça de Ferro","Cueca Estrelada","Calça Legging"])
        case 4:
            equipamento = random.choices(["Espadão","Vara de Moisés","Arco Longo"])
    equipamento = "".join(equipamento)
    return equipamento

def Equipando(Equipamento,Jogador):
    match Equipamento:
        case "Capacete":
            Jogador.Capacete()
            Jogador.AdicionandoEquipamento(1,Equipamento)
        case "Gorro":
            Jogador.Gorro()
            Jogador.AdicionandoEquipamento(1,Equipamento)
        case "Capuz":
            Jogador.Capuz()
            Jogador.AdicionandoEquipamento(1,Equipamento)
        case "Peitoral de Ferro":
            Jogador.PeitoralFerro()
            Jogador.AdicionandoEquipamento(2,Equipamento)
        case "Vestido Mágico":
            Jogador.VestidoMagico()
            Jogador.AdicionandoEquipamento(2,Equipamento)
        case "Roupa Camulfada":
            Jogador.RoupaCamuflada()
            Jogador.AdicionandoEquipamento(2,Equipamento)
        case "Calça de Ferro":
            Jogador.CalçaFerro()
            Jogador.AdicionandoEquipamento(3,Equipamento)
        case "Cueca Estrelada":
            Jogador.CuecaEstrelada()
            Jogador.AdicionandoEquipamento(3,Equipamento)
        case "Calça Legging":
            Jogador.CalçaLegging()
            Jogador.AdicionandoEquipamento(3,Equipamento)
        case "Espadão":
            Jogador.Espadão()
            Jogador.AdicionandoEquipamento(4,Equipamento)
        case "Vara de Moisés":
            Jogador.VaraDeMoises()
            Jogador.AdicionandoEquipamento(4,Equipamento)
        case "Arco Longo":
            Jogador.ArcoLongo()
            Jogador.AdicionandoEquipamento(4,Equipamento)