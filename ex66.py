n = 0
x = 0
con = 0
while n != 999:
    x = x + n
    n = int(input("Digite um número para somar(999 para parar): "))
    con = con + 1
print("A soma dos seus números é:",x)
print("E foram digitados",con,"números")
