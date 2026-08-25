# 5) Validação de Dados com Laço Indeterminado (Estruturas de Repetição)
# Enunciado: Escreva um programa que simule o cadastro de uma senha. O
# programa deve solicitar que o usuário digite uma senha de 4 dígitos numéricos.
# • Enquanto o usuário digitar uma senha que não tenha exatamente 4
# caracteres ou que não seja composta apenas por números, o programa
# deve exibir "Senha Inválida" e solicitar novamente.
# • Quando a senha for válida, exibir "Senha cadastrada com sucesso".
# ica: Use while e a função len() para verificar o comprimento.

senha = input("Digite uma senha de 4 dígitos: ")

while len(senha) != 4:
    print("Senha Inválida")
    senha = input("Digite uma senha de 4 dígitos: ")

print("Senha cadastrada com sucesso")