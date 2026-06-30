# Aula — Explorando o `for`

Na aula anterior aprendemos a utilizar o `for` juntamente com a função `range()`.

```python
for i in range(5):
    print(i)
```

Porém, o `for` é muito mais poderoso.

Ele pode percorrer praticamente qualquer conjunto de informações.

Nesta aula conheceremos algumas das formas mais comuns de utilizá-lo.

---

# O `for` com `range()`

Já conhecemos este formato.

```python
for i in range(5):
    print(i)
```

Resultado:

```
0
1
2
3
4
```

Também podemos definir início e fim.

```python
for i in range(10,16):
    print(i)
```

Resultado:

```
10
11
12
13
14
15
```

---

## Exercício

Imprima os números de 20 até 30.

---

# Definindo o passo

Também podemos informar de quanto em quanto queremos contar.

```python
for i in range(0,21,2):
    print(i)
```

Resultado:

```
0
2
4
6
8
...
20
```

O terceiro número do `range()` é chamado de **passo**.

---

## Exercício

Faça uma contagem:

- de 5 em 5 até 100;
- de 10 em 10 até 200;
- regressiva de 100 até 0.

---

# Percorrendo uma String

Uma string nada mais é do que uma sequência de caracteres.

Podemos percorrê-la utilizando o `for`.

```python
nome = "Python"

for letra in nome:
    print(letra)
```

Resultado:

```
P
y
t
h
o
n
```

---

## Exercício

Peça um nome ao usuário e imprima uma letra por linha.

---

# Contando letras

Também podemos utilizar o `for` para contar determinadas letras.

```python
texto = input("Digite uma frase: ")

contador = 0

for letra in texto:

    if letra == "a":
        contador += 1

print(contador)
```

---

## Exercício

Conte quantas letras "e" existem em uma frase.

---

# Introdução às listas

Até agora nossas variáveis armazenavam apenas um valor.

```python
nome = "João"
```

Mas podemos guardar vários valores ao mesmo tempo.

```python
frutas = [
    "Maçã",
    "Banana",
    "Laranja",
    "Morango"
]
```

Isso é chamado de **lista**.

---

# Percorrendo listas

```python
for fruta in frutas:
    print(fruta)
```

Resultado

```
Maçã
Banana
Laranja
Morango
```

Observe que não precisamos saber quantas frutas existem.

O `for` percorre todos os elementos automaticamente.

---

## Exercício

Crie uma lista contendo cinco cidades.

Utilize um `for` para imprimi-las.

---

# Somando números de uma lista

```python
numeros = [12,8,15,30,42]

soma = 0

for numero in numeros:

    soma += numero

print(soma)
```

---

## Exercício

Calcule a média dos números da lista.

---

# Introdução aos dicionários

Além das listas, existe outra estrutura muito utilizada: o dicionário.

Ele funciona como uma agenda.

Cada informação possui uma chave.

```python
aluno = {
    "nome":"Carlos",
    "idade":19,
    "curso":"Python"
}
```

---

# Percorrendo um dicionário

```python
for chave in aluno:
    print(chave)
```

Resultado

```
nome
idade
curso
```

Podemos acessar também os valores.

```python
for chave in aluno:
    print(aluno[chave])
```

Ou ambos.

```python
for chave, valor in aluno.items():
    print(chave,valor)
```

---

## Exercício

Crie um dicionário com informações sobre um carro.

Imprima:

- somente as chaves;
- somente os valores;
- chave e valor juntos.

---

# Resumo

Nesta aula aprendemos que o `for` pode percorrer:

- `range()`;
- Strings;
- Listas;
- Dicionários.

Nas próximas aulas utilizaremos essas estruturas para criar programas muito mais completos.
