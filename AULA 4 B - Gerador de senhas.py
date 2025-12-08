#Gerador de senhas 1
#Importando 2 bibliotecas
import random#Possibilitar fornecer valores aleatórios
import string#Possibilita inserir tipos de caracteres específicos
print("Gerador de Senha 1")
#Determinando o tamanho da senha
tamanho=int(input("Olá. Quantos caracteres deve ter a sua senha?"))
cara=string.digits#String digits determina que a senha terá apenas números
senha=' '.join(random.choice(cara) for _ in range (tamanho))
#join tem como função unir a função de escolha aleatória (random.choice) com o for
#por utilizar o for, a quantidade de valores aleatórios será o tamanho da senha
print(f"Sua senha gerada foi:\n {senha}")
