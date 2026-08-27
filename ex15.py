km_percorridos = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias utilizado: '))
total_a_pagar = (km_percorridos * 0.15) + (dias * 60)
print(f'O valor total a pagar é de R${total_a_pagar:.2f}')