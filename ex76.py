lista = ('lápis', 1.75,
         'borracha', 2,
         'caderno', 15,
         'estojo', 20,
         'mochila', 120)

print('=-'*20)
print(f'{"PREÇOS"}')
print('-='*20)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}')
    else:
        print(f'R${lista[pos]:>7.2f}')

