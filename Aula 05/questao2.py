# 2) Crie um programa em Python que lê uma
# lista de 10 nomes e sorteia um nome entre eles.
import random, os

nomes = []

for x in range(10):
    nome = input(f'Digite o {x+1}° Nome: ')
    nomes.append(nome)
    os.system('cls' or 'clear')
    
sortudo = random.choice(nomes)
print (f'Você {sortudo} foi o (a) sorteado (a)!')