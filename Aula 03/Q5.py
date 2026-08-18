import os
os.system("cls")


senha = 'python123'
senha_digitada = input("Digite a senha: ")

if senha_digitada == senha:
    print(f"Senha correta. ")
else:
    print(f"Senha incorreta. ")
