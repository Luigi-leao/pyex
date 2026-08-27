peso = float(input("Qual é seu peso?"))
altura = float(input("Qual sua altura?"))
imc = peso / (altura ** 2)
print("O IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc>= 18.5 and imc < 25:
    print("Você está com o peso ideal")
else:
    print("Você está acima do peso")