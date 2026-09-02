# Questão 5 — Caixa Eletrônico
# Crie um programa que simule um saque em um caixa eletrônico.
# O programa deverá solicitar:
# Saldo disponível
# • Valor do saque
# Depois deverá verificar:
# Se o valor do saque é válido.
# Se o valor solicitado é menor ou igual ao saldo.
# Se o saque pode ser realizado.
# Caso possa, apresentar o saldo restante.
# O programa deve utilizar try/except para tratar entradas que não sejam números.
# Exemplo:
# Digite seu saldo: 1000
# Digite o valor do saque: 300
# Saque realizado com sucesso!
# Saldo restante: 700
# Caso tente sacar mais do que possui:
# Digite seu saldo: 500
# Digite o valor do saque: 800
# Saldo insuficiente!
# Caso digite uma informação inválida:
# Digite seu saldo: quinhentos
# Erro: digite apenas valores numéricos!
import os

os.system("cls")

print("============ CAIXA ELETRÔNICO ============")

try:
    saldo = float(input("Digite seu saldo: "))
    saque = float(input("Digite o valor do saque: "))

    if saque <= 0:
        print("Valor de saque inválido!")
    elif saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - saque

        print("")
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: {saldo:.2f}")

except:
    print("Erro: digite apenas valores numéricos!")