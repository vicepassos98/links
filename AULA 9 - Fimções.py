#AULA 9 - Definindo funções e funções estátisticas
pets=[]

def cadastrar_pet(pets):# def é comando para definir uma função. A função se chama "cadastrar_pet"
#as informações dessa função vão ser armazenados na lista "pets"
    nome=input("Nome do pet")
    especie=input("Espécie:")
    idade=int(input("Idade em anos"))
    peso=float(input("Peso em kg"))
    porte=clas_porte(peso)#essa é uma função a ser definida
    pet={#pet é o nome da nossa biblioteca
    "nome":nome,#cada linha representa uma categoria da biblioteca
    "especie":especie,
    "idade":idade,
    "peso":peso,
    "porte":porte
    }
    pets.append(pet)#add a biblioteca à lista pets
    
def clas_porte(peso):
    if peso <5:
        return "pequeno"#Se o peso for menor que 5 o programa retorna "pequeno"
    elif peso <20:
        return "médio"
    else:
        return "GRANDE"

def mostrar_pets(pets):
    if len (pets)==0:
        print("Nenhum pet cadastrado")
        return
    else:
        print("Lista de cadastros:")
        print("-------------------")
        for p in pets:
            print(f"Nome: {p['nome']} - {p['especie']} - {p['idade']} anos")
            print(f"Peso: {p['peso']} kg - Porte: {p['porte']}")
            print("-------------------------------------")

def peso_medio(pets):
    if len(pets)==0:
        print("Nenhum pet cadastrado, impossível determinar média")
        return
    media=sum(p['peso'] for p in pets)/len(pets)
    print(f"A média de peso dos pets é de: {media:.2f} kg")
def extremos(pets):
    if len(pets)==0:
        print("Nenhum pet cadastrado")
        return
    peso_min=min(p['peso'] for p in pets)
    peso_max=max(p['peso'] for p in pets)
    pet_min=[p["nome"] for p in pets if p["peso"]==peso_min]
    pet_max=[p["nome"] for p in pets if p["peso"]==peso_max]
    print(f" {pet_min} é o pet mais leve com {peso_min} kg")
    print(f" {pet_max} é o pet mais pesado com {peso_max} kg")

while True:
    print("===PET DATA 2.2===")
    print()
    print("MENU DE COMANDOS")
    print("Cadastrar")
    print("Exibir")
    print("Media")
    print("Extremos")
    print("Apagar")
    print("Sair")
    print()
    op=input("Escreva o comando que quer executar:")
    if op.lower()=="cadastrar":
        cadastrar_pet(pets)
    elif op.lower()=="exibir":
        mostrar_pets(pets)
    elif op.lower()=="sair":
        print("Encerrando Programa")
        break
    elif op.lower()=="apagar":
        pets.clear()
        print("Lista limpa")
    elif op.lower()=="media":
        peso_medio(pets)
    elif op.lower()=="extremos":
        extremos(pets)
    else:
        print("Escreve esse trem direito queridão")
        
