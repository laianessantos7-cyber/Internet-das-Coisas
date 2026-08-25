#1) Crie um programa que lê uma lista de 10 números e conta a quantidade de
# números positivos e a quantidade de números negativos, e mostra o vetor
# com os negativos e o a soma dos positivos?
positivos = []
negativos = []
print('')

print( '============== POSITIVOS E NEGATIVOS =============')
for x in range (10):
    num = int (input(f"Digite o {x +1} º número: "))
    print('')
    if (num >= 0):
        positivos.append(num)
    else:
        negativos.append(num)
quantidade_positivo = len (positivos)
quantidade_negativo = len (negativos)
soma_positivos = sum(positivos)

print(f"Quantidade de números positivos: {quantidade_positivo}")
print('')
print(f"Quantidade de números negativos: {quantidade_negativo}")
print('')
print(f"Vetor com os negativos: {negativos}")
print('')
print(f"Soma dos positivos: {soma_positivos}")