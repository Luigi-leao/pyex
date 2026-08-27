sexo = str(input("Informe seu sexo (M ou F): "))

while sexo not in 'MmFf':
    sexo = str(input('Dados não aceitos, digite novamente. '))
    
print("Feito.")

