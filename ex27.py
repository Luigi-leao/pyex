nome = str(input("Digite seu nome inteiro: ")).strip()
separar = nome.split()
print("Primeiro nome: {}".format(separar[0]))
print("Ultimo nome: {}".format(separar[len(separar)-1]))
