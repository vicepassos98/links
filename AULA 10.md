# Aula 10 — Funções em Python

Até agora escrevemos programas colocando todo o código em sequência.

Essa estratégia funciona para programas pequenos, mas conforme eles crescem, começamos a repetir muitos trechos de código.

Para resolver esse problema utilizamos as **funções**.

Uma função é um bloco de código que executa uma tarefa específica e pode ser reutilizado quantas vezes forem necessárias.

Na verdade, você já utiliza funções desde a primeira aula.

```python
print("Olá!")
```

```python
len([1, 2, 3])
```

```python
np.mean(notas)
```

Todas essas funções foram criadas por outros programadores.

Nesta aula vamos aprender a criar as nossas próprias funções.

---

# Por que utilizar funções?

Imagine que precisamos calcular o dobro de vários números.

Sem utilizar funções:

```python
print(5 * 2)
print(8 * 2)
print(13 * 2)
print(22 * 2)
```

O código funciona.

Porém, imagine que agora o professor peça o triplo ao invés do dobro.

Será necessário alterar todas as linhas.

As funções resolvem justamente esse problema.

Escrevemos a lógica apenas uma vez e reutilizamos sempre que necessário.

---

# Estrutura de uma função

Toda função possui a seguinte estrutura:

```python
def nome_da_funcao(parametro):
    # código
    return resultado
```

Onde:

- `def` indica que estamos criando uma função;
- `nome_da_funcao` é o nome escolhido para ela;
- `parametro` representa a informação recebida pela função;
- `return` devolve o resultado.

---

# Criando nossa primeira função

Vamos criar uma função que calcula o dobro de um número.

```python
def dobro(numero):

    resultado = numero * 2

    return resultado
```

Agora podemos utilizá-la.

```python
print(dobro(5))
print(dobro(8))
print(dobro(13))
print(dobro(22))
```

Resultado:

```text
10
16
26
44
```

Observe que escrevemos a lógica apenas uma vez.

---

## Exercício 1

Crie uma função chamada `triplo()`.

Ela deve receber um número e retornar seu triplo.

Teste com cinco valores diferentes.

---

# Alterando a lógica

Se quisermos modificar o comportamento da função, basta alterar seu código.

Por exemplo:

```python
def dobro(numero):
    return numero * 3
```

Agora todas as chamadas da função passarão a calcular o triplo.

---

# Funções com vários parâmetros

Uma função pode receber mais de uma informação.

```python
def somar(a, b):

    return a + b
```

Utilizando a função:

```python
print(somar(3, 7))
print(somar(10, 25))
```

Resultado:

```text
10
35
```

---

## Exercício 2

Crie uma função chamada `multiplicar()`.

Ela deve receber dois números e retornar a multiplicação entre eles.

---

# Funções que retornam textos

O retorno não precisa ser um número.

Também podemos retornar uma string.

```python
def saudacao(nome):

    return "Olá, " + nome + "!"
```

Utilizando:

```python
mensagem = saudacao("Menestrel")

print(mensagem)
```

Resultado:

```text
Olá, Menestrel!
```

---

## Exercício 3

Crie uma função chamada `boas_vindas()`.

Ela deve receber o nome de uma pessoa e retornar uma mensagem personalizada.

---

# Funções sem retorno

Nem toda função precisa utilizar `return`.

Às vezes queremos apenas executar alguma ação.

```python
def linha():

    print("=" * 30)
```

Utilizando:

```python
linha()

print("Relatório")

linha()
```

Resultado:

```text
==============================
Relatório
==============================
```

Nesses casos, a função apenas executa comandos e não devolve nenhum valor.

---

## Exercício 4

Crie uma função chamada `titulo()`.

Ela deve imprimir:

```text
========================
CURSO DE PYTHON
========================
```

---

# Programa completo

Vamos criar um pequeno programa utilizando várias funções.

```python
def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


while True:

    print("\nCalculadora")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":

        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        print("Resultado:", somar(n1, n2))

    elif op == "2":

        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        print("Resultado:", multiplicar(n1, n2))

    elif op == "3":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")
```

Observe que o programa principal ficou muito menor.

Toda a lógica matemática está organizada dentro das funções.

---

# Desafio

Crie as seguintes funções:

- `quadrado(numero)` → retorna o quadrado do número;
- `media(a, b, c)` → retorna a média de três valores;
- `maior(a, b)` → retorna o maior entre dois números;
- `par(numero)` → retorna `True` caso o número seja par e `False` caso seja ímpar.

Depois crie um programa que utilize todas elas.

---

# Resumo

Nesta aula aprendemos:

- o que são funções;
- por que elas evitam repetição de código;
- como criar funções com `def`;
- como utilizar parâmetros;
- como utilizar `return`;
- funções que retornam números;
- funções que retornam textos;
- funções que apenas executam comandos.

        
