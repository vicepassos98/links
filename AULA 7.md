# Aula 7 — Trabalhando com listas paralelas

Na aula anterior aprendemos a criar e manipular listas.

Até agora, cada lista armazenava apenas um tipo de informação.

Por exemplo:

```python
destinos = [
    "Dubai",
    "Alasca",
    "Irã"
]
```

Mas imagine um sistema de estoque.

Precisamos guardar **o nome do produto** e também **a quantidade disponível**.

Uma única lista não é suficiente para isso.

Nesta aula vamos utilizar **listas paralelas**.

Cada posição de uma lista corresponderá à mesma posição da outra.

Exemplo:

| Posição | Produtos | Quantidade |
|---------:|----------|-----------:|
| 0 | Arroz | 10 |
| 1 | Feijão | 20 |
| 2 | Açúcar | 15 |

Observe que:

- `produtos[0]` corresponde a `quantidades[0]`;
- `produtos[1]` corresponde a `quantidades[1]`;
- e assim por diante.

---

# Criando duas listas

Primeiro, crie duas listas vazias.

```python
produtos = []
quantidades = []
```

Uma armazenará os nomes dos produtos.

A outra armazenará suas respectivas quantidades.

---

## Exercício 1

Crie as duas listas acima e exiba seu conteúdo utilizando `print()`.

Resultado esperado:

```text
[]
[]
```

---

# Adicionando produtos

Vamos adicionar um produto e sua quantidade inicial.

```python
nome = input("Nome do produto: ")
qtd = int(input("Quantidade inicial: "))

produtos.append(nome)
quantidades.append(qtd)
```

Agora podemos verificar as listas.

```python
print(produtos)
print(quantidades)
```

---

## Exercício 2

Cadastre três produtos diferentes.

Ao final, exiba as duas listas.

---

# Percorrendo listas paralelas

Como mostrar o nome e a quantidade ao mesmo tempo?

Utilizamos um `for` juntamente com a função `len()`.

```python
for i in range(len(produtos)):
    print(f"{produtos[i]}: {quantidades[i]} unidades")
```

Vamos entender esse código.

A função:

```python
len(produtos)
```

retorna a quantidade de elementos existentes na lista.

Se houver quatro produtos cadastrados, teremos:

```text
0
1
2
3
```

A variável `i` representa cada uma dessas posições.

Assim, quando:

```text
i = 0
```

o programa acessa:

```python
produtos[0]
quantidades[0]
```

Quando:

```text
i = 1
```

ele acessa:

```python
produtos[1]
quantidades[1]
```

E assim sucessivamente.

---

## Exercício 3

Cadastre cinco produtos.

Depois utilize o `for` acima para listar todo o estoque.

---

# Localizando um produto

Agora imagine que queremos alterar apenas um produto.

Primeiro precisamos verificar se ele existe.

```python
nome = input("Produto: ")

if nome in produtos:
    print("Produto encontrado.")
else:
    print("Produto não encontrado.")
```

O operador `in` verifica se um elemento pertence à lista.

---

## Exercício 4

Teste o programa digitando:

- um produto existente;
- um produto inexistente.

Observe o resultado.

---

# Descobrindo a posição do produto

Depois de localizar um produto, precisamos descobrir sua posição na lista.

Para isso utilizamos `.index()`.

```python
indice = produtos.index(nome)

print(indice)
```

Exemplo:

Se a lista for:

```text
Arroz
Feijão
Macarrão
```

e o usuário digitar:

```text
Feijão
```

o resultado será:

```text
1
```

---

## Exercício 5

Cadastre quatro produtos.

Digite um deles e descubra sua posição utilizando `.index()`.

---

# Alterando uma quantidade

Agora podemos modificar o estoque.

```python
indice = produtos.index(nome)

quantidades[indice] += 5
```

O operador `+=` adiciona um valor ao conteúdo existente.

Também podemos diminuir uma quantidade.

```python
quantidades[indice] -= 3
```

---

## Exercício 6

Cadastre um produto.

Adicione 10 unidades.

Depois retire 4 unidades.

Confira o resultado.

---

# Programa completo — Gestor de Estoque

Agora que conhecemos:

- listas paralelas;
- `append()`;
- `len()`;
- `in`;
- `index()`;
- operadores `+=` e `-=`;

podemos desenvolver um pequeno sistema de controle de estoque.

```python
print("=== GESTOR DE ESTOQUE ===")

produtos = []
quantidades = []

while True:

    print("\nMenu")
    print("1 - Cadastrar produto")
    print("2 - Mostrar estoque")
    print("3 - Dar baixa")
    print("4 - Adicionar quantidade")
    print("5 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":

        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade inicial: "))

        produtos.append(nome)
        quantidades.append(qtd)

        print(f"{nome} cadastrado com {qtd} unidade(s).")

    elif op == "2":

        print("\n=== ESTOQUE ===")

        for i in range(len(produtos)):
            print(f"{produtos[i]}: {quantidades[i]} unidade(s)")

    elif op == "3":

        nome = input("Produto: ")

        if nome in produtos:

            indice = produtos.index(nome)

            qtd_baixa = int(input("Quantidade: "))

            if qtd_baixa <= quantidades[indice]:

                quantidades[indice] -= qtd_baixa

                print("Baixa realizada.")

            else:

                print("Quantidade insuficiente.")

        else:

            print("Produto não encontrado.")

    elif op == "4":

        nome = input("Produto: ")

        if nome in produtos:

            indice = produtos.index(nome)

            qtd_add = int(input("Quantidade: "))

            quantidades[indice] += qtd_add

            print("Quantidade adicionada.")

        else:

            print("Produto não encontrado.")

    elif op == "5":

        print("Programa encerrado.")

        break

    else:

        print("Digite uma opção válida.")
```

---

# Desafio

Implemente as seguintes melhorias:

- impedir o cadastro de produtos com o mesmo nome;
- não permitir quantidades negativas;
- mostrar o total de produtos cadastrados;
- mostrar a soma de todas as unidades em estoque;
- criar uma opção para remover completamente um produto do sistema.
