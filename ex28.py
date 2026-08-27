from random import randint
num = randint(0,5)
guess = int(input("Qual numero o computador ta pensando?: "))
if num==guess:
    print("Voce acertou")
else:
    print("Voce errou! Era o numero ", num)
