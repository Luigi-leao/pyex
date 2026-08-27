from random import randint


print("Tente adivinhar!")

num = randint(0,10)
tentativas = 0
certo = False

while certo == False:
    usuario = int(input('Digite um numero: '))
    tentativas = tentativas + 1 

    if usuario == num:
        certo = True
    else: 
        print("Tente mais uma vez!")

print("Você Acertou com {} tentativas".format(tentativas))
