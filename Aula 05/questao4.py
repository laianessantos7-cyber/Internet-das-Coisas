# 4) Desenvolva um programa que peça números ao usuário até que ele digite 0,
# e então exiba a soma de todos os números digitados.


numeros= []
print('=============== SOMADOR INFINITO ===============')
while True:
    
    num = int (input('Digite um número: '))
    if (num!=0):
        numeros.append(num)
    else:
        break
soma = sum (numeros)
print('')
print(f'A Soma dos números digitados é: {soma} ')