numero = int(input("Digite o numero: "))
uni = numero // 1 % 10
deze = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print("milhar: {}".format(mil))
print("centena: {}".format(cen))
print("dezena: {}".format(deze))
print("unidade: {}".format(uni))