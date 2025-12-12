estoque=[]
while True:
    print("===Estoquer 2000===")
    print("1 - Adcionar ao Estoque")
    print("2 - Ver Estoque")
    print("3 - Limpar Estoque")
    print("4 - Sair")
    entrada=input("Selecione uma das opções:")
    if entrada =="1":
        quantidade=int(input("Quantas produtos serão cadastradas"))
        for i in range(quantidade):
            print(f"Produto {i+1}")
            nome=input("Nome:")
            qtd=int(input("Quantidade:"))
            custo=float(input("Custo:"))
            preco=float(input("Preço:"))
            produtos={
            "nome":nome,
            "quantidade":qtd,
            "custo":custo,
            "preco":preco
            }
            estoque.append(produtos)
            
            print("Cadastro concluido")
    elif entrada =="2":
        if not len(estoque)==0:
            print("Estoque Cadastrado")
            for p in estoque:     
                print(f"Nome: {p['nome']} | Quantidade: {p['quantidade']}| Custo: {p['custo']}| Preço: {p['preco']}")
        else:
            print("Estoque Vazio")
    elif entrada=="3":
        estoque.clear()
        print("Seu estoque está limpo")
    elif entrada=="4":
        print("Programa Encerrado")
        print("...See you again...")
        break
    else:
        print("20 ANOS DE CURSO, É SÓ DIGITAR O NÚMEROZINHO PÔ")
