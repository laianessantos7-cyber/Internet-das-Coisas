import os
os.system("cls")

print("===Calculadora ===")

n1= float (input("Digite o primeiro número:  "))
n2= float (input("Digite o segundo número:  "))
operador=(input("Digite uma operação (+, -, * ou /):"))

soma =n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1 / n2



if operador== "+":
    result = n1 + n2

elif operador == "-":
    result = n1-n2
elif operador == "*":
    result = n1 * n2
elif operador == "/":
    result  = n1/n2

if n2 !=0:
    resultado = n1/n2

print(f"O resultado da operação é:  {result}" )
