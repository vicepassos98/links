# Aula 6 — Trabalhando com listas

Até agora, todas as variáveis que criamos armazenavam apenas **um único valor**.

Por exemplo:

```python
nome = "Victor"
idade = 27
```

Mas imagine um programa que precise guardar vários destinos de viagem, vários alunos, vários produtos ou vários filmes.

Criar uma variável para cada item seria inviável.

Para resolver esse problema utilizamos as **listas**.

Uma lista permite armazenar vários valores em uma única variável.

---

# Criando uma lista

Para criar uma lista vazia utilizamos colchetes `[]`.

```python
destinos = []
```

Observe que a variável continua sendo criada com o sinal de igualdade (`=`), porém agora o valor atribuído é uma lista vazia.

---

## Exercício 1

Crie uma lista chamada `filmes`.

Em seguida, utilize `print()` para verificar seu conteúdo.

```python
filmes = []

print(filmes)
```

Resultado esperado:

```text
[]
```

---

# Adicionando itens

Para adicionar novos elementos utilizamos o método `.append()`.

```python
destinos.append("Dubai")
destinos.append("Alasca")
destinos.append("Irã")
destinos.append("Xique-Xique - BA")
```

Agora podemos visualizar a lista.

```python
print(destinos)
```

Resultado:

```text
['Dubai', 'Alasca', 'Irã', 'Xique-Xique - BA']
```

---

## Exercício 2

Crie uma lista chamada `jogos`.

Adicione cinco jogos diferentes utilizando `.append()`.

Depois exiba a lista.

---

# Adicionando itens com `input()`

Também podemos adicionar informações digitadas pelo usuário.

```python
destinos = []

novo = input("Digite um destino: ")

destinos.append(novo)

print(destinos)
```

---

## Exercício 3

Faça o usuário cadastrar três frutas.

Ao final, exiba a lista.

---

# Removendo itens

Para remover um elemento utilizamos `.remove()`.

```python
destinos.remove("Irã")
```

Agora a lista ficará assim:

```text
['Dubai', 'Alasca', 'Xique-Xique - BA']
```

---

## Exercício 4

Remova um dos itens da lista criada anteriormente.

Observe o resultado.

> **Importante:** o item precisa existir na lista. Caso contrário ocorrerá um erro.

---

# Limpando toda a lista

Para apagar todos os elementos utilizamos `.clear()`.

```python
destinos.clear()
```

Agora:

```python
print(destinos)
```

Resultado:

```text
[]
```

---

## Exercício 5

Crie uma lista com cinco cidades.

Depois utilize `.clear()`.

Confira se a lista ficou vazia.

---

# Percorrendo listas

Já conhecemos o `for`.

Ele também funciona perfeitamente com listas.

```python
destinos = [
    "Dubai",
    "Alasca",
    "Irã"
]

for destino in destinos:
    print(destino)
```

Resultado:

```text
Dubai
Alasca
Irã
```

---

## Exercício 6

Crie uma lista contendo cinco animais.

Utilize um `for` para imprimir um animal por linha.

---

# Numerando os elementos

Às vezes queremos mostrar a posição de cada elemento.

Para isso utilizamos `enumerate()`.

```python
for i, destino in enumerate(destinos, start=1):
    print(f"{i} - {destino}")
```

Resultado:

```text
1 - Dubai
2 - Alasca
3 - Irã
```

O parâmetro `start=1` faz com que a numeração comece em 1.

Caso ele seja omitido, a contagem começará em 0.

---

## Exercício 7

Crie uma lista contendo cinco filmes.

Utilize `enumerate()` para numerá-los.

---

# Programa completo — Gerenciador de Destinos

Agora que conhecemos:

- listas;
- `.append()`;
- `.remove()`;
- `.clear()`;
- `for`;
- `enumerate()`;

podemos construir um pequeno sistema para gerenciar destinos de viagem.

```python
print("=== GERENCIADOR DE DESTINOS 6.7 ===")

destinos = []

while True:

    print("\nEscolha uma opção:")
    print("1 - Adicionar destino")
    print("2 - Remover destino")
    print("3 - Visualizar destinos")
    print("4 - Limpar lista")
    print("5 - Encerrar")

    entrada = input("Opção: ")

    if entrada == "1":

        item = input("Digite o destino: ")

        destinos.append(item)

        print(f"{item} foi adicionado.")

    elif entrada == "2":

        retirar = input("Destino a remover: ")

        if retirar in destinos:
            destinos.remove(retirar)
            print(f"{retirar} foi removido.")
        else:
            print("Destino não encontrado.")

    elif entrada == "3":

        if len(destinos) == 0:
            print("Nenhum destino cadastrado.")
        else:
            for i, item in enumerate(destinos, start=1):
                print(f"{i} - {item}")

    elif entrada == "4":

        destinos.clear()

        print("Lista limpa.")

    elif entrada == "5":

        print("Até a próxima!")

        break

    else:

        print("Digite uma opção válida.")
```

---

# Desafio

Modifique o programa para que:

- o usuário não consiga cadastrar o mesmo destino duas vezes;
- o programa informe quantos destinos existem na lista;
- antes de apagar toda a lista, o programa pergunte:

```text
Tem certeza? (S/N)
```

Somente apague a lista se o usuário responder **S**.
    notas.append(f"{entrada} {snome}: {média} - {sit}")
