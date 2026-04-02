print("===Sistema de Notas===")
notas=[]
while True:
    entrada=input("Insira o nome do aluno ou 'sair' para encerrar ou 'lista' para ver as notas")
    if entrada.lower()=="sair":
        print("O programa está sendo encerrado")
        break
    if entrada.isdigit():
        print("Insira o nome do aluno, não a nota")
        continue
    if entrada.lower()=="lista":
        for i, entrada in enumerate (notas, start=1):
            print(f"{i} - {entrada}")
        continue
    snome=input("Insira o sobrenome do aluno")
    nota1=float(input("insira a primeira nota"))
    nota2=float(input("insira a segunda nota"))
    nota3=float(input("inisra a terceira nota"))
    média=(nota1+nota2+nota3)/3
    print()
    print(f"A média do(a) aluno(a) {entrada} {snome} é: {média}")
    if média >=5:
        sit="Aprovado"
    else:
        sit="Reprovado"
    print()
    print(f" O(A) aluno(a) {entrada} {snome} está: {sit}")
    print()
    notas.append(f"{entrada} {snome}: {média} - {sit}")
