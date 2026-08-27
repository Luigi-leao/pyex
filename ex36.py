salario = float(input("Digite seu salário: R$"))
trinta = (salario / 100) * 30
casa = float(input("Digite o valor da casa: R$"))
parcelas = float(input("Em quantas parcelas quer pagar a casa? "))
vp = casa / parcelas
if vp > trinta:
    print("O empréstimo foi negado")
else:
    print("O empréstimo foi aceito")
    