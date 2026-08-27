from datetime import date
idade = date.today().year
nasce = int(input("Digite seu ano de nascimento: "))
verdadeira = idade - nasce
if verdadeira <=9:
    print ("Participará do ramo mirim")
elif verdadeira <=14:
    print ("Participará do ramo infantil")
elif verdadeira <=19:
    print ("Participará do ramo junior")
elif verdadeira <=25:
    print ("Participará do ramo senior")
else:
    print ("Participará do ramo master")
print("O participante tem {}".format(verdadeira))
