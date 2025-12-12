#Aula 8 - Dicionários
#Definindo Nomes e idades da turma
while True:  
    print("1 - Cadastrar")
    print("2 - Exibir")
    print("3 - Sair")
    print("4 - Limpar")
    entrada=input("Insir a função desejada")
    
    if entrada =="1":
        pessoas=[]#Lista principal
        total_idade=0#para calcular a média
        quantidade=int(input("Quantas pessoas serão cadastradas?"))
        for i in range(quantidade):
            print(f"Pessoas {i+1}")
            nome=input("Nome:")
            idade=int(input("Idade:"))
            pessoa={
            "nome":nome,
            "idade":idade
            }#no caso a biblioteca vai ser composta por duas variáveis: nome e idade
            pessoas.append(pessoa)
            #o total de idade vai ser igual a soma das idades
            print("Cadastro concluido")
    if entrada=="2":
        print("----Pessoas Cadastradas----")
        for p in pessoas:
        # o p indica que para cada elemento da lista ele irá
        #demonstrar uma característica específica deste elemento
            print(f"Nome: {p['nome']} | Idade: {p['idade']}")
    if entrada=="3":
        print("adeus")
        break
    if entrada=="4":
        pessoas.clear()
        print("lista limpa com sucesso")
