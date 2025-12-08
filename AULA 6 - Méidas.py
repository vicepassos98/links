#Sistema de notas: calcula a média e indica a situação do aluno
print("===Sistema de Notas 2.2.1===")
print()
#Criando o looping para o Prof inserir várias notas
while True:
    nome=input("Insira o nome do aluno, ou digite sair para encerrar o programa")
    if nome.lower()=="sair":
        print("Encerrando programa\n.................")
        break
    snome=input("Insira o sobrenome do aluno")
    nota1=float(input(f" Insira a primeira nota do(a) aluno(a) {nome} {snome}:"))
    nota2=float(input("Insira a segunda nota:"))
    nota3=float(input("Insira a terceira nota:"))
    nota4=float(input("Insira a quarta nota:"))
    media=(nota1+nota2+nota3+nota4)/4
    print(f"A nota média final do(a) aluno(a) é de {media:.2f}")#limitar a qtde de casas decimais
    if media >=9:
        sit="MB - Muito Bom"
    elif media >=7:
        sit="B - Bom"
    elif media >=5:
        sit="R - Regular"
    else:
        sit="I - Irregular"
    print()
    print(f" A situação do(a) aluno(a) é:\n.....{sit}.....")
