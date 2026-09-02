# Questão 1 — Calculadora de Soma
# Crie um programa que solicite ao usuário dois números e mostre a soma deles.
# O programa deve utilizar try/except para impedir que o programa seja encerrado caso o usuário digite algo que não seja um número. 
# Exemplo:
# Digite o primeiro número: 10
# Digite o segundo número: 5
# Resultado: 15
# Caso seja digitado um valor inválido:
# Digite o primeiro número: dez
# Erro: digite apenas números !


import os

os.system("cls")

print("===Calculadora ===")

while True:
    try:
        n1 = int(input("Digite o 1 número: "))
        n2 = int(input("Digite o 2 número: "))

        soma = n1 + n2
        print("Resultado:", soma)
        break

    except:
        print("Dados inválidos! Somente números.")
        