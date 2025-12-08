#Tabuada Automática
# Entrada de dados através de input
# lAÇOS (for) e repetições (while)
print("Tabuada mais fácil")
numero=int(input("digite um número inteiro: "))
print(f"Tabuado do {numero}: ")
for v in range(1,11):
    print(f"{numero} x {v} = {numero*v}")

#Tabuada Automática, porém um cadin mais complexa
print("Tabuada 2: o inimigo agora é outro")
while True:
    entrada = input("Digite um número ou 'sair' para encerrar.")
    if entrada=="sair":
        print("\nPrograma Encerrado")
        break 
    if not entrada.isdigit():
        print("Por favor, digite um núemro válido")
        continue
    numero = int(entrada)
    print(f"Tabuada do {numero}: ")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
    print("\n")
