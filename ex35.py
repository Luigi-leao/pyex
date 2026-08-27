x = float(input("Digite um lado do triângulo: "))
y= float(input("Digite outro lado do triângulo: "))
z = float(input("Digite o último lado do triângulo: "))
if x > y and x > z:
    w = y + z
    if w > x:
        print("Tem como fazer um triângulo com esses valores")
    else: 
        print("Não tem como fazer um triângulo com esses valores")
if y > x and y > z:
    w = x + z
    if w > y:
        print("Tem como fazer um triângulo com esses valores")
    else: 
        print("Não tem como fazer um triângulo com esses valores")
if z > x and z > y:
    w = x + y
    if w > z:
        print("Tem como fazer um triângulo com esses valores")
    else: 
        print("Não tem como fazer um triângulo com esses valores")
