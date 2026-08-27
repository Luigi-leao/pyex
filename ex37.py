n = int(input("Digite um número inteiro: "))

print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    resultado = bin(n)
    print(f"O número {n} em binário é: {resultado}")
elif opcao == 2:
    resultado = oct(n)
    print(f"O número {n} em octal é: {resultado}")
elif opcao == 3:
    resultado = hex(n)
    print(f"O número {n} em hexadecimal é: {resultado}")
else:
    print("Opção inválida. Escolha 1, 2 ou 3 para a base de conversão.")
