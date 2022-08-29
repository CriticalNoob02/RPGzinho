import random
from Gerar_Nomes import GerarNome, Nome
## varL == variaveis listas para as escolhas.

###################################################################### Classe Pai (Base do Mundo / Quantidades / Nomes);

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
        numReinos = random.randint(3,6)
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

###################################################################### Classes Filhos (Caracteristicas Gerais dos Ambientes);

class Reinos(Mundo):
    def __init__(self):
        super().__init__()
        self.tamanho = []
        self.localização = []
        self.ameaça = []
        self.rei = []
    
    def GerarCaracteristicas(self):
        for i in self.reinos:
            ## Escolhendo;
            tamanhoL = random.choices(["Pequeno","Médio","Grande","Gigante"])
            localizaçãoL = random.choices(["Deserto","Oceano","Ártico","Floresta","Montanha"])
            ameaçaL = random.choices(["Aliados","Mercador","Passivos","Ameaçadores","Rivais"])
            nomeRei = Nome()
            ## Transcrevendo;
            tamanho =''.join(tamanhoL)
            localização =''.join(localizaçãoL)
            ameaça =''.join(ameaçaL)
            ## Adicionando;
            self.tamanho.append(f"{tamanho}")
            self.localização.append(f"{localização}")
            self.ameaça.append(f"{ameaça}")
            self.rei.append(nomeRei)

    def MostrarReinosGeral(self):
        i = 0
        for reinos in self.reinos:
            print("")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f" Reino Nº{i}")
            print(f" Nome: {self.reinos[i]}")
            print(f" Rei: {self.rei[i]}")
            print(f" Tamanho: {self.tamanho[i]}")
            print(f" Localização: {self.localização[i]}")
            print(f" Relação: {self.ameaça[i]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")
            i += 1
        
    def MostrarReino(self,i):
        for reinos in self.reinos:
            print("")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f" Reino Nº{i}")
            print(f" Nome: {self.reinos[i]}")
            print(f" Rei: {self.rei[i]}")
            print(f" Tamanho: {self.tamanho[i]}")
            print(f" Localização: {self.localização[i]}")
            print(f" Relação: {self.ameaça[i]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")

class Vilas(Mundo):
    def __init__(self):
        super().__init__()
        self.tamanhoV = []
        self.localizaçãoV = []

    def GerarCaracteristicasVila(self):
        for i in self.vilas:
            ## Escolhendo;
            tamanhoL = random.choices(["Pequena","Média","Grande"])
            localizaçãoL = random.choices(["Deserto","Oceano","Ártico","Floresta","Montanha","Pantano","Caverna","Ilha"])
            ## Transcrevendo;
            tamanho =''.join(tamanhoL)
            localização =''.join(localizaçãoL)
            ## Adicionando;
            self.tamanhoV.append(tamanho)
            self.localizaçãoV.append(localização)
    
    def MostrarVilasGeral(self):
        i = 0
        for vila in self.vilas:
            print("")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f" Vila Nº{i}")
            print(f" Nome: {self.vilas[i]}")
            print(f" Tamanho: {self.tamanhoV[i]}")
            print(f" Localização: {self.localizaçãoV[i]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")
            i += 1

    def MostrarVila(self, i):
        for vila in self.vilas:
            print("")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f" Vila Nº{i}")
            print(f" Nome: {self.vilas[i]}")
            print(f" Tamanho: {self.tamanhoV[i]}")
            print(f" Localização: {self.localizaçãoV[i]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")

class Florestas(Mundo):
    def __init__(self):
        super().__init__()
        self.caracteristicasF = []
    
    def GerarCaracteristicasFlorestas(self):
        for i in self.florestas:
            ## Escolhendo;
            caracteristicasL = random.choices(["Negra","Amaldiçoada","Abençoada","Densa","Tropical","Gélida","Oásis",])
            ## Transcrevendo;
            caracteristicas =''.join(caracteristicasL)
            self.caracteristicasF.append(caracteristicas)

    def MostrarFlorestasGeral(self):
        i = 0
        for floresta in self.florestas:
            print("")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f" Floresta Nº{i}")
            print(f" Nome: {self.florestas[i]}")
            print(f" Caracteristicas: {self.caracteristicasF[i]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")
            i += 1

    def MostrarFloresta(self,i):
        for floresta in self.florestas:
            print("")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f" Floresta Nº{i}")
            print(f" Nome: {self.florestas[i]}")
            print(f" Caracteristicas: {self.caracteristicasF[i]}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("")
            i += 1


mundo = Florestas()

mundo.GerarMundo()
mundo.MostrarMundo()
mundo.GerarCaracteristicasFlorestas()
mundo.MostrarFlorestasGeral()
