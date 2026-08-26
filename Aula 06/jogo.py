import random, os , time

numero_secreto = random.randint(1,100) # Sorteando Numero.
tentativas = 0

while True:
    numero = int(input('Diigite o Número Secreto: '))
    tentativas+=1
    if (numero == numero_secreto):
        print(f'🎉 Parabéns você ACERTOU o número em {tentativas} tentativas!')
        break
    elif(numero_secreto>numero):
        print(f'O número secreto é maior!! - {tentativas} tentativas')
        time.sleep(3)

        os.system('cls' or 'clear')
    else:
        print(f'O número secreto é menor!! - {tentativas} tentativas')
        time.sleep(3)
        os.system('cls' or 'clear')
    
