n = int(input("Primeiro termo: \n"))
razao = int(input("Digite a razão da PA: \n"))
termo = n + (10 - 1) * razao
for x in range(n, termo + razao, razao):
    print("{}".format(x), end=" ")
