import random, os , time

numero_secreto = random.randint(1,100) # Sorteando Numero.
tentativas = 5


while True:
    numero = int(input('Diigite o Número Secreto: '))
    tentativas+=1
    if (numero == numero_secreto):
        print(f'🎉 Parabéns você ACERTOU o número em {tentativas} tentativas!')
        break
    elif (tentativas == 5):
            print('Gamer Over! Você não tem mais tentativas!')
            break
    elif(numero_secreto>numero):
        print(f'O número secreto é maior!! - {tentativas} tentativas')
        time.sleep(2)
    
        os.system('cls' or 'clear')
    else:
        print(f'O número secreto é menor!! - {tentativas} tentativas')
        time.sleep(2)
        os.system('cls' or 'clear')
    
