# Aula 4 — Estruturas de repetição

Até agora, todos os programas que desenvolvemos possuem um comportamento semelhante:

1. O programa inicia;
2. O usuário realiza uma operação;
3. O programa termina.

Se quisermos utilizá-lo novamente, precisamos executá-lo outra vez.

Imagine se fosse necessário reiniciar o WhatsApp toda vez que você quisesse enviar uma mensagem. Não faria muito sentido.

Na maioria das aplicações, esperamos que o programa continue funcionando até que o usuário decida encerrá-lo.

Para resolver esse problema utilizamos as **estruturas de repetição**, também conhecidas como **loops**.

---

# O `while`

A palavra **while** significa **"enquanto"**.

Enquanto uma condição for verdadeira, o bloco de código será executado repetidamente.

Observe o exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
```

Resultado:

```text
1
2
3
4
5
```

Observe que, a cada repetição, a variável `contador` aumenta em uma unidade.

Quando o contador passa a valer `6`, a condição deixa de ser verdadeira e o programa continua normalmente.

---

## Exercício 1

Altere o programa anterior para que ele conte de **1 até 10**.

---

## Exercício 2

Agora faça o programa contar de **5 até 15**.

---

## Exercício 3

Faça o programa contar de **10 até 1**.

> **Desafio:** Qual linha do código precisou ser alterada para fazer a contagem regressiva?

---

# O `while True`

Também podemos criar um laço infinito.

```python
while True:
    print("Olá!")
```

Esse programa nunca terminará sozinho.

Para encerrá-lo é necessário utilizar outro comando: o `break`.

---

# O comando `break`

O comando **break** encerra imediatamente um laço de repetição.

Observe:

```python
while True:

    texto = input("Digite 'sair' para encerrar o programa: ")

    if texto == "sair":
        break

print("Programa encerrado.")
```

Agora o programa continuará funcionando até que o usuário digite a palavra **sair**.

---

## Exercício 4

Modifique o programa para que ele seja encerrado somente quando o usuário digitar:

```text
fim
```

---

# O comando `continue`

O comando `continue` também interrompe uma repetição, porém de forma diferente.

Enquanto o `break` encerra completamente o laço, o `continue` apenas interrompe a repetição atual e volta imediatamente para o início do `while`.

Observe:

```python
while True:

    texto = input("Digite alguma coisa: ")

    if texto == "":
        continue

    print(texto)

    if texto == "sair":
        break
```

Se o usuário apenas pressionar **Enter**, o programa voltará para o início sem imprimir nada.

---

## Exercício 5

Execute o programa acima e experimente:

- pressionar apenas **Enter**;
- digitar uma palavra qualquer;
- digitar **sair**.

Observe o comportamento do programa em cada situação.

---

# Validando entradas com `.isdigit()`

Nem sempre o usuário digitará um número.

O método `.isdigit()` verifica se um texto é composto apenas por dígitos.

Exemplo:

```python
entrada = input("Digite um número: ")

print(entrada.isdigit())
```

Experimente digitar:

- `25`
- `abc`
- `3.5`
- `-10`

Observe quais retornam `True` e quais retornam `False`.

> **Importante:** o método `.isdigit()` reconhece apenas números inteiros positivos.

---

## Exercício 6

Faça um programa que peça um número ao usuário.

Enquanto ele digitar algo que **não seja um número inteiro**, o programa deverá solicitar novamente.

---

# Padronizando textos com `.lower()`

Os usuários podem digitar respostas de várias maneiras.

Por exemplo:

```text
SIM
Sim
sIm
siM
```

Para evitar problemas, podemos transformar todas as letras em minúsculas utilizando o método `.lower()`.

Exemplo:

```python
resposta = input("Deseja continuar? ")

print(resposta.lower())
```

Independentemente da forma como o usuário escrever, o resultado será:

```text
sim
```

---

## Exercício 7

Faça um programa que permaneça em execução até que o usuário digite:

```text
sair
```

O programa deve aceitar qualquer combinação de letras maiúsculas e minúsculas, como:

- SAIR
- Sair
- saiR
- SaIr

---

# Programa completo — Sistema de pedidos do Mr. Dog

Agora que conhecemos `while`, `break`, `continue`, `.isdigit()` e `.lower()`, podemos construir um programa mais completo.

```python
while True:
    print("==== MR. DOG ====")
    print("1 - Dog Simples....R$12,00")
    print("2 - Dog Duplo......R$18,00")
    print("3 - Encerrar Programa")

    dog = input("Selecione uma opção: ")

    if dog == "1":
        vdog = 12
        ndog = "Dog Simples"

    elif dog == "2":
        vdog = 18
        ndog = "Dog Duplo"

    elif dog == "3":
        print("Adeus...")
        print("Programa encerrado.")
        break

    elif not dog.isdigit():
        print("Digite apenas números.")
        continue

    else:
        print("Opção inválida.")
        continue

    qtde = int(input("Quantidade desejada: "))

    print(f"Você escolheu {qtde} unidade(s) de {ndog}.")
    print(f"Total: R${vdog * qtde},00\n")
```

---

# O laço `for`

O `while` é utilizado quando **não sabemos quantas vezes** o programa deverá repetir.

Já o `for` é utilizado quando **sabemos exatamente a quantidade de repetições**.

Observe:

```python
for i in range(5):
    print(i)
```

Resultado:

```text
0
1
2
3
4
```

O comando `range(5)` gera cinco valores:

```text
0, 1, 2, 3 e 4
```

---

## Exercício 8

Faça o programa imprimir os números de **1 até 5**.

---

## Exercício 9

Imprima os números de **1 até 10**.

---

## Exercício 10

Imprima apenas os números pares de **2 até 20**.

---

## Exercício 11

Faça uma contagem regressiva de **10 até 1**.

---

## Exercício 12

Utilizando o `for`, imprima cinco vezes a frase:

```text
Python é incrível!
```

---

# Programa completo — Tabuada automática

Agora vamos utilizar o `while`, o `for` e tudo o que aprendemos até aqui para construir uma tabuada automática.

```python
print("=== TABUADA AUTOMÁTICA ===")

while True:

    entrada = input("Digite um número ou 'sair' para encerrar: ")

    if entrada.lower() == "sair":
        print("Programa encerrado.")
        break

    if not entrada.isdigit():
        print("Digite apenas números inteiros positivos.")
        continue

    numero = int(entrada)

    print(f"\nTabuada do {numero}\n")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    print()
```

---

# Resumo da aula

Nesta aula aprendemos:

- utilizar o `while`;
- criar laços infinitos com `while True`;
- encerrar um laço utilizando `break`;
- reiniciar um laço utilizando `continue`;
- validar entradas com `.isdigit()`;
- padronizar textos utilizando `.lower()`;
- utilizar o `for`;
- utilizar `range()` para controlar repetições.

As estruturas de repetição estão entre os recursos mais importantes da programação. A partir delas será possível desenvolver programas muito mais completos e automatizados.
