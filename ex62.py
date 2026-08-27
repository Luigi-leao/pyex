ter = int(input("informe o primeiro termo da PA: "))
ra = int(input("informe a razão da PA: "))

con = 1

x = 1
con2 = 1

while con <= 10:
    ter = ter + ra
    print(ter)
    con = con + 1

while x != 0:
    x = int(input("quantos números a mais vocÊ quer na sequencia?(se não pressione 0)"))

    while con2 <= x:
        ter = ter + ra
        print(ter)
        con2 = con2 + 1
    con2 = 1
