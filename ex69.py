id18 = 0
mas = 0
mul20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = ""
    while sexo not in "MF":
        sexo = str(input("Sexo[M/F]: ")).upper().strip()[0]
    if idade >= 18:
        id18 += 1
    if sexo == "M":
        mas += 1
    if sexo == "F" and idade < 20:
        mul20 += 1

    rp = ""
    while rp not in "SN":
        rp = str(input("Deseja continuar[S/N]? ")).upper().strip()[0]
    if rp == "N":
        break


print("Pessoas com mais de 18 anos:",id18,".")
print("total de homens:",mas,".")
print("Foram cadastradas",mul20,"com menos de 20 anos.")
