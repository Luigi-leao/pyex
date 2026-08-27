salario = float(input("Qual o seu salário: R$"))
if salario <= 1250:
    x = salario / 100
    y = x * 15 
    salario2 = y + salario 
    print("o salário com aumento fica: R$", salario2)
else:
    x = salario / 100
    y = x * 10
    salario2 = y + salario 
    print("o salário com aumento fica: R$", salario2)
