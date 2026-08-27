
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
   
    if lado1 == lado2 and lado1 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"

   
    print("Tem como formar um triângulo do tipo", tipo_triangulo)
else:
    print("Não tem como formar um triângulo")
