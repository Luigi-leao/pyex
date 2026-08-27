resp = 's'
soma = con =maior = menor = 0

while resp in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    con += 1
    if con == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input("Deseja continuar?(S/N)")).upper().strip()[0]

med = soma / con
print("Foram digitados",con,"números, e a média foi",med)
print("Sendo o maior número",maior,",e o menor",menor)
print("Fim")
