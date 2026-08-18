import os
os.system("cls")

salario = float(input("Digite o salário: "))

salario_alto = 5000

if salario > salario_alto:
    print("Salário alto")
else:
    print("Salário dentro da média")