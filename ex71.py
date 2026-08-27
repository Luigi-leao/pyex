valor = int(input("Qual o valor a ser retirado?"))
valor50 = valor20 = valor10 = valor1 = con = 0

while valor != 0:
    if con == 0:
        valor50 = valor // 50
        valor = valor % 50
        con += 1

    if con == 1:
        valor20 = valor // 20
        valor = valor % 20
        con += 1
    
    if con == 2:
        valor10 = valor // 10
        valor = valor % 10
        con += 1

    if con == 3:
        valor1 = valor // 1
        valor = valor % 1
        con += 1

print("\nSERÃO IMPRESSAS: ")
print("Notas de 50:",valor50)
print("Notas de 20:",valor20)
print("Notas de 10:",valor10)
print("Notas de 1:",valor1)

