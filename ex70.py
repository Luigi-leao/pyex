total = cont = overk = 0
menor = float
meno = str
rp = str

while True:
    nome = str(input("Qual o nome do se produto? "))
    preço = float(input("Qual foi o preço do produto? "))
    total += preço

    if cont == 0:
        menor = preço
    if preço > 1000:
        overk += 1
    if preço < menor:
        menor = preço
        meno = nome

    cont += 1
    rp = " "
    while rp not in "SN":
        rp = str(input("Deseja continuar[S/N]? ")).upper().strip()[0]
    if rp == "N":
        break

print("Você gastou",total,"reais.")
print("Foram comprados",overk,"itens mais caros que 1000 reais")
print("O item mais barato custou",menor)
