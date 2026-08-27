n1 = float(input("Digite um número: \n"))
n2 = float(input("Digite outro número: \n"))

maior = 0
menor = 0

menu = ('''\n[1] Somar
     [2] Multiplicar
     [3] Maior ou menor
     [4] Escolher novos números
     [5] Encerrar\n ''')


print(menu)


escolha = int(input("Selecione: \n"))
while escolha != 5:
    if escolha == 1:  
        print("Resultado da soma: \n{} + {} = {}".format(n1, n2, (n1 + n2)))
        print(menu)
        escolha = int(input("Sua escolha: \n"))
    elif escolha == 2: 
        print("\n{} x {} = {}".format(n1, n2, (n1 * n2)))
        print(menu)
        escolha = int(input("Sua escolha: \n"))
    elif escolha == 3: 
        if n1 > n2:
            maior = n1
            menor = n2
            print("O maior é {} e o menor é {}.".format(n1, n2))
            print(menu)
        elif n2 > n1:
            maior = n2
            menor = n1
            print("O maior é {} e o menor é {}.".format(n2, n2))
            print(menu)
        else:
            print("Os dois números são iguais.")
            print(menu)
            escolha = int(input("Sua escolha: \n"))
    elif escolha == 4:
            outron1 = float(input("Novo número: \n"))
            outron2 = float(input("Novo número: \n"))
            n1 = outron1
            n2 = outron2
            print(menu)
            escolha = int(input("Sua escolha: \n"))

print("Opção 5: programa encerrado.")


