# Questão 2 — Verificador de Idade
# - Crie um programa que solicite a idade de uma pessoa.
# O programa deverá:
# Utilizar try/except para tratar uma entrada inválida.
# Verificar se a pessoa é menor de idade ou maior/igual a 18 anos.
# Exemplo:
# Digite sua idade: 16
# Você é menor de idade.
# Entrada inválida:
# Digite sua idade: abc
# Erro: digite uma idade válida!

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 18:
            print("Você é menor de idade.")
            break
        else:
            print("Você é maior de idade.")
            break

    except:
        print("Erro: digite uma idade válida!")