# Aula 8 — Dicionários

Até agora trabalhamos com listas e listas paralelas.

Essas estruturas funcionam bem quando temos poucos dados, mas começam a ficar difíceis de gerenciar quando a informação cresce.

Por exemplo, em um sistema de estoque:

- Arroz → 20 unidades  
- Feijão → 15 unidades  
- Macarrão → 8 unidades  

Se quisermos adicionar mais informações, como preço, fornecedor e validade, precisaríamos criar várias listas paralelas, o que torna o código confuso e difícil de manter.

Para resolver esse problema, usamos os **dicionários**.

---

# O que é um dicionário?

Um dicionário é uma estrutura que armazena dados no formato:

```
chave → valor
```

Cada informação possui uma **chave única**, que aponta para um valor específico.

---

# Primeiro exemplo

```python
produto = {
    "nome": "Arroz",
    "quantidade": 20,
    "preco": 18.50
}
```

---

# Acessando valores

Para acessar um valor, usamos a chave correspondente:

```python
print(produto["nome"])
print(produto["quantidade"])
```

---

# Alterando valores

Podemos modificar valores diretamente:

```python
produto["quantidade"] = 50
```

Ou atualizar valores existentes:

```python
produto["quantidade"] += 10
```

---

## Exercício 1

Crie um dicionário chamado `carro` com:

- modelo  
- ano  
- preço  

Depois altere o preço do carro.

---

# Dicionário com pessoas

```python
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Python"
}
```

---

## Exercício 2

Crie um dicionário chamado `aluno` com seus dados.

Depois imprima apenas o nome.

---

# Dicionários dentro de dicionários

Podemos armazenar estruturas mais complexas:

```python
pessoas = {
    "João": {
        "idade": 40,
        "curso": "Power BI"
    },
    "Lucas": {
        "idade": 30,
        "curso": "Python"
    }
}
```

---

# Acessando dados aninhados

```python
print(pessoas["Lucas"]["curso"])
```

---

## Exercício 3

Crie um dicionário com pelo menos 3 pessoas.

Cada pessoa deve conter:

- idade  
- curso  

Depois acesse uma informação específica.

---

# Lista de dicionários

Agora vamos combinar listas com dicionários.

```python
pessoas = [
    {"nome": "Ana", "idade": 20},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Lucas", "idade": 18}
]
```

---

# Percorrendo a lista

```python
for pessoa in pessoas:
    print(pessoa["nome"])
```

---

## Exercício 4

Crie uma lista com 3 alunos.

Cada aluno deve ser um dicionário com nome e idade.

Depois imprima todos os nomes usando `for`.

---

# Programa completo — Cadastro de pessoas

Agora vamos juntar tudo em um sistema simples.

```python
pessoas = []

while True:

    print("\n=== MENU ===")
    print("1 - Cadastrar")
    print("2 - Exibir")
    print("3 - Sair")
    print("4 - Limpar")

    entrada = input("Escolha uma opção: ")

    if entrada == "1":

        nome = input("Nome: ")
        idade = int(input("Idade: "))

        pessoa = {
            "nome": nome,
            "idade": idade
        }

        pessoas.append(pessoa)

        print("Cadastro concluído.")

    elif entrada == "2":

        print("\n=== Pessoas cadastradas ===")

        for p in pessoas:
            print(f"Nome: {p['nome']} | Idade: {p['idade']}")

    elif entrada == "3":

        print("Adeus...")
        break

    elif entrada == "4":

        pessoas.clear()
        print("Lista limpa com sucesso.")

    else:

        print("Opção inválida.")
```

---

# Desafio

Melhore o programa:

- impedir nomes duplicados  
- calcular média de idade  
- mostrar total de pessoas cadastradas  
- permitir remover uma pessoa pelo nome  

---

# Conexão com a próxima aula

Até aqui, você aprendeu a organizar dados de forma manual com listas e dicionários.

Na próxima etapa, vamos transformar isso em algo muito mais poderoso: **tabelas e análise de dados com pandas**.
```
