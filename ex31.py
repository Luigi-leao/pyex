preco = float (0.50)
preco2 = float (0.45)
km = float(input("Qual a distância da viagem? "))
if km <= 200:
    valor = preco * km
    print ("O preço da viagem ficara R$",valor)
else:
    valor = preco2 * km  
    print ("O preço da viagem ficara R$",valor)  
