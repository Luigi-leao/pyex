from random import randint

opcoes = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0,2)

print("Escolha: (0)Pedra (1)Papel (2)Tesoura")
jogador = int(input("Qual jogada você fará? "))

print(f"\nO computador escolheu {opcoes[bot]}")
print(f"Você escolheu {opcoes[jogador]}""\n")

if bot == 0:
    if jogador == 0:
        print("EMPATE")

    elif jogador == 1:
        print("VOCÊ VENCEU")

    elif jogador == 2:
        print("VOCÊ PERDEU")

    else:
        print("Jogada inválida.")

if bot == 1:
    if jogador == 0:
        print("VOCÊ PERDEU")

    elif jogador == 1:
        print("EMPATE")

    elif jogador == 2:
        print("VOCÊ VENCEU")

    else:
        print("Jogada inválida.")

if bot == 2:
    if jogador == 0:
        print("VOCÊ VENCEU")

    elif jogador == 1:
        print("VOCÊ PERDEU")

    elif jogador == 2:
        print("EMPATE")

    else:
        print("Jogada inválida.")

