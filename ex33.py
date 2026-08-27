n1 = float(input("Escreva um número: "))
n2 = float(input("Escreva outro número: "))
if n1 > n2:
    print(n1,"É o maior e", n2, "é o menor")
elif n2>n1:
    print(n2,"É o maior e", n1, "é o menor")
elif n2==n1:
    print("Os números possuem o mesmo valor")
