# Questão 3:
# Tabuada
# Crie um programa que solicite um número inteiro e mostre sua tabuada de 1 até 10.
# O programa deve utilizar:
# try/except Variável input
# Estrutura de repetição
# Caso o usuário digite algo que não seja um número inteiro, o programa deverá informar que a entrada é inválida.
# Exemplo:
# Digite um número: 7
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 10 = 70

print('========== TABUADA ==========')
while True:
    
    try:
        n = int(input("Digite um número: "))

        for x in range(1, 11):
            resultado = n * x
            print(n, "x", x, "=", resultado)

        break

    except:
        print("ERRO! Somente números inteiros.")