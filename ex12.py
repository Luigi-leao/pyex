produto = float(input('Digite o valor do produto: '))
desconto = produto * 0.05
produto_com_desconto = produto - desconto
print(f'O valor do produto com desconto de 5% é R${produto_com_desconto:.2f}, você economizou R${desconto:.2f}.')