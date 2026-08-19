import os
os.system('cls')

carrinho = []
print("======== BEM-VINDO AO MERCADINHO, BOAS COMPRAS! ========")
print('')

while True:
    

    produto = float(input('Digite o valor do produto: '))
    if ( produto == 0):
        break
    else:
        carrinho.append(produto)
        print(f'Produto {produto} adicionado ao carrinho.')

total=sum(carrinho)
print(f'Valor total da sua compra é R$: {total:.2f}')
print("======== VOLTE SEMPRE. ========")
