#Criar um programa que cria e gerencia uma lista
lista=[]#É a sintaxe para criar uma lista
while True:
    print()
    print("Menu")
    print("1 - Adicionar Destino")
    print("2 - Remover Destino")
    print("3 - Ver lista completa")
    print("4 - Limpar lista")
    print("5 - Sair")
    print()
    entrada=input("Escolha uma opção:")
    if entrada=="1":
        item=input("Digite seu destino:")
        lista.append(item)#append é a função para adicionar o item na lista
        print(f" {item} foi adicionado a sua lista de destinos")
    elif entrada=="2":
        item=input("Digite o destino a remover da lista")
        lista.remove(item)#remove retira um item da lista
        print(f" {item} foi retirado da sua lista de destinos")
    elif entrada=="3":
        print("Veja abaixo sua lista completa:")
        if len(lista)==0:#len indica o tamanho da lista, se for 0, indica que não há itens
            print("Sua lista está vazia")
        else:
            for i, item in enumerate(lista, start=1):#Enumerando os itens da lista
                print(f"{i} . {item}")
    elif entrada=="4":
        lista.clear#o comando para apagar a lista
        print("Sua lista está vazia")
    elif entrada=="5":
        print("Encerrando Programa. ADEUS")
        break#Encerra o looping que inicamos no while True
    else:
        print("Opção inválida. Insira SOMENTE um número de 1 a 5 querido")
