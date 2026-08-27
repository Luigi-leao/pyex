frase = str(input("Digite para verificar o palíndromo: \n"))
frase = "".join(frase.split(" "))
print("A palavra {} ao contrário é {}, ou seja, ".format(frase, frase[::-1]), end="")
if frase == frase[::-1]:
    print("é um palíndromo.".format(frase))
else:
    print("não é um palíndromo.".format(frase))
