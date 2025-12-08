#sistema de gestão de estoques. Um sistema com listas duplas
print("=== Gestor de Estoques 1.1 ===")
produtos=[]
quantidades=[]
while True:
    print("Menu: Controle de estoque")
    print("1 - Cadastrar produto")
    print("2 - Mostrar Estoque")
    print("3 - Dar baixa em produto")
    print("4 - Adicionar Quantidade")
    print("5 - Sair")
    op=input("Escolha uma opção")
    #Cadastrando produtos
    if op=="1":
        nome=input("Insira o nome do produto")
        qtd=int(input("Insira a quantidade inicial"))
        produtos.append(nome)#adiciona o input "nome" a lista "produtos"
        quantidades.append(qtd)#adiciona o input "qtd" a lista "quantidades"
        print(f"O produto {nome} foi cadastrado")
    #Visualizando o Estoque:
    elif op=="2":
        print()
        print("==Estoque Atual==")
        for i in range(len(produtos)):
            #o for será executado pela mesma quantidade de itens da lista de produtos.
            #o len será igual a quantidade de itens na lista, ou seja seu comprimento.
            print(f"{produtos[i]}:{quantidades[i]} unidades")# quando i=1, o programa mostrará o primeiro item da lista produtos e da lista quantidades
    elif op=="3":#BAIXAR QTD DE PRODUTOS
        nome=input("Qual produto deseja baixar?")
        if nome in produtos:#temos que saber se o nome está na lista de produtos
            indice=produtos.index(nome)#a função index determina a posição da entrada (nome) dentro da lista "produtos"
            qtd_baixa=int(input("Quantas unidades deseja baixar?"))
            if qtd_baixa<=quantidades[indice]:#antes de baixar temos que ter certeza que a quantidade baixada é menor ou igual a quantidade atual
                quantidades[indice]-=qtd_baixa#vamos subtrair a qtd baixada da qtd atual. A nova qtd atual será o resultado da subtração
                print("Baixa realizada")
            else:
                print("Quantidade insuficiente")
        else:
            print("Produto não encontrado")
    elif op=="4":#ADCIONAR QTD DE PRODUTOS
        nome=input("Qual produto deseja adicionar?")
        if nome in produtos:
            indice=produtos.index(nome)
            qtd_add=int(input("Quantidade a adicionar:"))
            quantidades[indice]+=qtd_add#adicionamos a qtd deseja a quantidade atual e salvamos o resultado como nova qtd atual
            print("Quantidade adicionada")
        else:
            print("Produto não encontrado")
    elif op=="5":#saindo dessa bomba
        print("..Encerrando o Programa..")
        print(".........................")
        print("..........Adeus!.........")
        break#finalizar o looping
    else:
        print("Opção inválida digite um número de 1 a 5")
