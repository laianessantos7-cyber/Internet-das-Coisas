# Questão 4
# Sistema de Notas
# Crie um programa que solicite 3 notas de um aluno.
# O programa deverá:
# 1. Ler as três notas.
# 2. Calcular a média.
# 3. Verificar:
# Média maior ou igual a 7 → Aprovado
# Média entre 5 e 6.9 Recuperação
# Média menor que 5 Reprovado
# 4. Utilizar try/except para tratar entradas inválidas.
# Exemplo:
# Digite a primeira nota: 8
# Digite a segunda nota: 6
# Digite a terceira nota: 7
# Média: 7.0
# Situação: Aprovado
# Se o aluno digitar:
# Digite a primeira nota: oito
# Erro: digite apenas números !
import os

os.system("cls")

print('============ SISTEMA DES NOTAS ============ ')
try:
    n1 = float(input("Digite a primeira nota: "))

    n2 = float(input("Digite a segunda nota: "))

    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3

    if media >= 7:
        resultado = "Aprovado!"
    elif media >= 5:
        resultado = "Recuperação!"
    else:
        resultado = "Reprovado!"

    print("")
    print(f"Média: {media:.1f}")
    print("")
    print(f"Situação: {resultado}")

except:
    print("Erro! Digite apenas números.")