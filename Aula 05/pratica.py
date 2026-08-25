#  Peça ao usuário para digitar 5 temperaturas (uma por uma) e guarde-as em uma lista.
# Use um laço para a entrada de dados.
# Após a leitura, exiba:
#A maior temperatura registrada (max).
# A menor temperatura registrada (min).
# A média das temperaturas.

temperatura = []

for x in range (5):
    temp = float(input(f'Digite a {x+1}ª Temperatura: '))
    temperatura.append(temp)
    
media = sum (temperatura) / len (temperatura)
menor = min (temperatura)
maior = max (temperatura)
    
print(f'A Maior temperatura do dia foi {maior} °C')
print (f'A Menor temperatura do dia foi {menor} °C')
print (f'A Média de temperatura do dia foi {media:.1f} °C')