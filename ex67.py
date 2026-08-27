x=1
while 0 < x:
    x = int(input("Escolha um número(números negativos encerrarão o programa): \n"))
    con = 1
    while con <= 10:
        pr = con * x
        print(pr)
        con += 1
print("Fim")
