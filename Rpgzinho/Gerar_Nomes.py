import random
###

def GerarNome():
    vogais = ["a","e","i","o","u",""]
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","w","z",""]
    nomeL = []
    nome = ""
    silabas = random.randint(1,4)

    for i in range(0,silabas):
        nomeL += random.choices(consoantes)
        nomeL += random.choices(vogais)

    nome =''.join(nomeL)
    nome = nome.capitalize()
    return nome

def GerarSobrenome():
    sobrenomeL = ["Phareman","Boschetti","Scariot","Thybaut","Gautzelin","Godfree","Girardus","Gerould","Gualterius","Gocelinus","Urhan","Ugovras","Azadium","Chavez","Olzoxon","Da Silva","Santos","Nubis","Skullblood","Geimadra"]
    sobrenome = random.choices(sobrenomeL)
    sobrenome = ''.join(sobrenome)
    
    return sobrenome

def Nome():
    PrimeiroNome = GerarNome()
    sobrenome = GerarSobrenome()

    nome = (f"{PrimeiroNome} {sobrenome}")
    
    return nome


