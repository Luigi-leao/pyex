from os import kill
from random import randint
vic = True
con = 0
while vic == True:
    itens = 'Pedra','Papel','tesoura'
    computador = randint(0,2)
    print("Pedra[0]"
    "Papel[1]"
    "Tesoura[2]")
    jogador = int(input("Sua escolha: "))
    print('computador: {}'.format(itens[computador]))

    if computador == 0:

        if jogador ==0:
            print("empate\n")
            con -= 1

        if jogador ==1:
            print("jogador vence\n")

        if jogador ==2:
            print("computador vence\n")
            print("Você venceu",con,"partidas")
            print("desenvolvido por: luigi")
            print("rm: 25116")
            vic = False

    elif computador == 1:

        if jogador ==0:
            print("computador vence\n")
            print("Você venceu",con,"partidas")
            print("desenvolvido por: luigi")
            print("rm: 25116")
            vic = False
        
        if jogador ==1:
            print("empate\n")
            con -= 1

        if jogador ==2:
            print("jogador vence\n")

    elif computador == 2:

        if jogador ==0:
            print("jogador vence\n")

        if jogador ==1:
            print("computador vence\n")
            print("Você venceu",con,"partidas")
            print("desenvolvido por: luigi")
            print("rm: 25116")
            vic = False

        if jogador ==2:
            print("empate\n")
            con -= 1
        
    con += 1
