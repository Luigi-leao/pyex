oposto = int(input("Escreva o valor cateto oposto: "))
adjacente = int(input("Escreva o valor do cateto adjacente: "))
opos2 = oposto * oposto
adja2 = adjacente * adjacente
hipotenusa = opos2 + adja2
realhip = hipotenusa ** (1/2)
print ("O valor da hipotenusa é de", realhip)