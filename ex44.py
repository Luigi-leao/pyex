def calcular_valor_final(preco_normal, forma_pagamento):
    if forma_pagamento == "dinheiro" or forma_pagamento == "cheque":
        valor_final = preco_normal - (preco_normal * 0.1)
        return valor_final
    elif forma_pagamento == "cartão":
        opcao = input("Digite a opção de parcelamento (1 para à vista, 2 para 2x, 3 para 3x ou mais): ")
        if opcao == "1":
            valor_final = preco_normal - (preco_normal * 0.05)
            return valor_final
        elif opcao == "2":
            valor_final = preco_normal
            return valor_final
        elif opcao == "3":
            valor_final = preco_normal + (preco_normal * 0.2)
            return valor_final
        else:
            print("Opção inválida!")
    else:
        print("Forma de pagamento inválida!")


preco_produto = float(input("Digite o preço do produto: "))
forma_pagamento = input("Digite a forma de pagamento (dinheiro, cheque ou cartão): ")

valor_final = calcular_valor_final(preco_produto, forma_pagamento)
print("O valor a ser pago é: %.2f" % valor_final)
