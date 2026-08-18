import os
os.system("cls")



a = int (input("Digite 1ª número:  "))
b = int (input("Digite 2ª número:  "))

if a > b:
    print(f"O primeiro número é maior que o segundo. ")

elif a < b:
    print(f"O segundo número é maior que o primeiro. ")

else:
    print(f"Os dois números são iguais! ")