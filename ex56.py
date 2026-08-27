soma = 0
idade = 0
homem = ''
mulheres = 0

for r in range(1, 5):
    print(" {}ª Pessoa ".format(r))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M ou F): ")).strip()
    soma += idade
    if r == 1 and sexo in 'Mm':
        media = idade
        homem = nome
    if sexo in 'Mm' and idade > media:
        media = idade
        homem = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
media = soma / 4

print('A média de idade do grupo é de {} anos'.format(media))
print("O homem mais velho é {} e tem {} anos".format(homem, idade))
print("{} Mulher(es) com menos de 20 anos".format(mulheres))

