# Aula 3 — Construindo um sistema de pedidos

Até agora aprendemos:

- criar variáveis;
- utilizar `print()` e `input()`;
- trabalhar com operadores de comparação;
- utilizar estruturas condicionais (`if`, `elif` e `else`).

Nesta aula vamos colocar tudo isso em prática desenvolvendo um pequeno sistema de pedidos para uma lanchonete.

Nosso programa permitirá que o cliente escolha:

- um hambúrguer;
- uma bebida;
- um acompanhamento.

Após cada escolha, o programa mostrará o valor parcial do pedido.

---

# Conhecendo o cardápio

Primeiro, vamos criar o nome da nossa lanchonete.

```python
print("==== DEBUG BURGER ====")
```

Agora vamos exibir o cardápio de hambúrgueres.

```python
print("Selecione seu hambúrguer:")
print("1 - X-Burger.............R$20,00")
print("2 - X-Bacon..............R$25,00")
print("3 - X-Bug................R$39,00")

hamburger = input("Digite o número do hambúrguer: ")
```

Execute a célula.

---

# Definindo o preço do hambúrguer

Agora utilizaremos uma cadeia de condicionais para descobrir qual foi o item escolhido.

```python
if hamburger == "1":
    ph = 20

elif hamburger == "2":
    ph = 25

elif hamburger == "3":
    ph = 39

else:
    print("Digite um número válido.")
    exit()
```

Observe a indentação.

As linhas recuadas pertencem à condição imediatamente acima delas.

Por exemplo:

```python
if hamburger == "1":
    ph = 20
```

A variável `ph` receberá o valor `20` apenas quando o usuário escolher a opção `1`.

Agora exiba o valor parcial do pedido.

```python
print(f"Até agora o valor do seu pedido é de R${ph},00")
```

---

# Escolhendo a bebida

Agora vamos repetir o mesmo processo para as bebidas.

```python
print("Escolha sua bebida:")

print("1 - Sprite............R$12,00")
print("2 - Coca Zero.........R$12,00")
print("3 - Água com gás......R$8,00")
print("4 - Nenhuma")

bebida = input("Digite o número da bebida: ")
```

Agora descubra o preço.

```python
if bebida == "1":
    pb = 12

elif bebida == "2":
    pb = 12

elif bebida == "3":
    pb = 8

elif bebida == "4":
    pb = 0

else:
    print("Digite um número válido.")
    exit()
```

Calcule o novo valor parcial.

```python
pf2 = ph + pb

print(f"Até agora o valor do seu pedido é de R${pf2},00")
```

---

# Escolhendo o acompanhamento

Agora faremos exatamente o mesmo processo.

```python
print("Escolha seu acompanhamento:")

print("1 - Batata Frita................R$15,00")
print("2 - Batata com cheddar e bacon..R$23,00")
print("3 - Anéis de cebola.............R$20,00")
print("4 - Nenhum")

acp = input("Digite o número do acompanhamento: ")
```

Agora determine o preço.

```python
if acp == "1":
    pa = 15

elif acp == "2":
    pa = 23

elif acp == "3":
    pa = 20

elif acp == "4":
    pa = 0

else:
    print("Digite um número válido.")
    exit()
```

---

# Calculando o preço final

Agora basta somar o valor do acompanhamento ao valor parcial.

```python
pf3 = pf2 + pa

print(f"O valor total do seu pedido é de R${pf3},00")
```

---

# O que aprendemos?

Neste exercício utilizamos diversas estruturas que já conhecemos:

- `print()`;
- `input()`;
- variáveis;
- operadores de comparação;
- `if`;
- `elif`;
- `else`;
- expressões matemáticas.

Perceba que o mesmo padrão foi repetido três vezes:

1. mostrar o cardápio;
2. receber a escolha do usuário;
3. utilizar uma condicional para descobrir o preço;
4. atualizar o valor do pedido.

Essa repetição será muito importante nas próximas aulas.

---

# Desafio

Até agora nosso programa informa apenas o preço do pedido.

Seria possível mostrar também o nome dos produtos escolhidos?

Por exemplo:

```text
==== DEBUG BURGER ====

Hambúrguer: X-Bacon
Bebida: Coca Zero
Acompanhamento: Batata Frita

Total: R$52,00
```

**Pense nas seguintes perguntas:**

- Além do preço, qual outra informação precisaríamos guardar em uma variável?
- Em qual parte do programa essa variável deveria receber um valor?
- Como poderíamos utilizar uma **f-string** para exibir todas essas informações ao final do programa?

> Não é necessário resolver o desafio agora. Ele servirá como preparação para os próximos conteúdos.
