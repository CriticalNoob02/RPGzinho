import random
from Gerar_Nomes import GerarNome

###################################################################### Classe Pai (Base do Inimigo);

class Mundo:
    def __init__(self):
        self.reinos = []
        self.oceanos = []
        self.lagos = []
        self.vilas = []
        self.florestas = []
        self.montanhas = []
        self.descartes = []
        self.minas = []
        self.cavernas = []
        self.mistérios = []

    def GerarMundo(self):
        ## Gerando Quantidade;
        numReinos = random.randint(1,6)
        numOceanos = random.randint(1,3)
        numLagos = random.randint(1,6)
        numVilas = random.randint(7,12)
        numFlorestas = random.randint(5,9)
        numMontanhas = random.randint(1,4)
        numDescartes = random.randint(0,3)
        numMinas = random.randint(2,7)
        numCavernas = random.randint(3,5)
        numMistérios = random.randint(1,8)

        ## Gerando Nomes e Adicionando na Lista;
        for i in range(0,numReinos):
            nome = GerarNome()
            self.reinos.append(f"Reino de {nome}")
        for i in range(0,numOceanos):
            nome = GerarNome()
            self.oceanos.append(f"Oceano {nome}")
        for i in range(0,numLagos):
            nome = GerarNome()
            self.lagos.append(f"Lago de {nome}")
        for i in range(0,numVilas):
            nome = GerarNome()
            self.vilas.append(f"Vila de {nome}")
        for i in range(0,numFlorestas):
            nome = GerarNome()
            self.florestas.append(f"Floresta de {nome}")
        for i in range(0,numMontanhas):
            nome = GerarNome()
            self.montanhas.append(f"Montanha {nome}")
        for i in range(0,numDescartes):
            nome = GerarNome()
            self.descartes.append(f"Lixão {nome}")
        for i in range(0,numMinas):
            nome = GerarNome()
            self.minas.append(f"Mina de {nome}")
        for i in range(0,numCavernas):
            nome = GerarNome()
            self.cavernas.append(f"Caverna de {nome}")
        for i in range(0,numMistérios):
            self.mistérios.append(f"Mistério {i+1}")

    def MostrarMundo(self):
        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")
        print(f"Parabens, seu Mundo foi gerado com sucesso!")
        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Reinos: {self.reinos}")
        print(f"Oceanos: {self.oceanos}")
        print(f"Lagos: {self.lagos}")
        print(f"Vilas: {self.vilas}")
        print(f"Florestas: {self.florestas}")
        print(f"Montanhas: {self.montanhas}")
        print(f"Descartes: {self.descartes}")
        print(f"Minas: {self.minas}")
        print(f"Cavernas: {self.cavernas}")
        print(f"Mistérios: {self.mistérios}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")

mundo = Mundo()

mundo.GerarMundo()
mundo.MostrarMundo()