#Aula 3 - A melhor calculadora do mundo (talvez não)
print("Calculadora Simples")
#Vamos criar os inputs para os usuários inserirem os números
num1=float(input("Digite o primeiro número:\n"))
num2=float(input("Digite o segundo número:\n"))#float limita a entrada a números
#Escolhendo as operações matemáticas
print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
operacao=input("Digite o número da operação desejada:")
if operacao=="1":
    resultado=num1+num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao=="2":
    resultado=num1-num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao=="3":
    resultado=num1*num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao=="4":
    if num2==0:
        print("Erro no sistema alguém me desconfigurou.\nNão é possível dividir por ZERO")
    else: resultado=num1/num2
    print(f"Resultado: {num1} / {num2} = {resultado}")
else: print("Operação Inválida. Digite um número de 1 a 4")
