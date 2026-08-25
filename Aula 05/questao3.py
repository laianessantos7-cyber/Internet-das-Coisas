# 3) Escreva um programa que leia uma lista de 5 nomes e depois exiba esses nomes em ordem alfabética.

nomes = []

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

nomes.sort()

print("Nomes em ordem alfabética:")
print(nomes)