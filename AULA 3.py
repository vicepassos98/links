#Sistema de pedidos para nossa lanchonete
#Vamos reforçar o uso do if, elif e else. Assim como o print e input
print("=== RATO NA GRELHA ===")
#Primeiro vamos inserir as opções de hamburgers
print("Selecione o seu Lanche:\n")
print("1 - X-Burger    R$20,00")
print("2 - X-Bacon     R$25,00")
print("3 - X-Ratão     R$39,00")
lanche=input("Insira o número do seu lanche")
#determinar o valor de acordo com a entrada do usuário
if lanche=="1":
    pl=20
elif lanche=="2":
    pl=25
elif lanche=="3":
    pl=39
else:
    print("Digite o número referente ao seu lanche")
    exit()
qtde=int(input("Quantos desse lanche você deseja?"))
rl=qtde*p1
print(f" Até agora o valor do seu pedido é de R${rl},00")
#Vamos definir nosso cardápio de bebidas
print("\nEscolha Sua Bebida:")
print("1 - Guarana Jesus  R$8,00")
print("2 - Coca Zero      R$10,00")
print("3 - Água C/ gás    R$7,00")
print("4 - Nenhuma")
bebida=input("Insira o número da sua bebida:\n")
if bebida=="1":
    pb=8
elif bebida=="2":
    pb=10
elif bebida=="3":
    pb=7
elif bebida=="4":
    pb=0
else:
    print("Digite o número CORRETO da sua bebida sô")
    exit()
qb=input("quantas bebidas?")
rb=pb*qb
fb=rb+rl
print(f"Até agora o valor do seu pedido é de R${fb},00")
#Agora vamos definir nosso cardápio de Acompanhamentos
print("Escolha seu acompanhamento:\n")
print("1 - Batata Frita              R$15,00")
print("2 - Batata c/ cheddar e bacon R$23,00")
print("3 - Aneis de Cebola           R$20,00")
print("4 - Nenhum")
acp=input("Insira o número do seu Acompanhamento:")
if acp=="1":
    pa=15
elif acp=="2":
    pa=23
elif acp=="3":
    pa=20
elif acp=="4":
    pa=0
else:
    print("Digite somente o número do seu acompanhamento")
    exit()
qa=input("quantos acompanhamentos você deseja?")
ra=rb+pa*qa
print(f"O preço do seu pedido é de R${p2},00.")
