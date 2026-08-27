from datetime import date


ano_atual = date.today().year


ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade < 18:
    anos_faltando = 18 - idade
    print("Ainda falta", anos_faltando, "anos para o alistamento militar.")
elif idade == 18:
    print("Está na hora de se alistar ao serviço militar!")
else:
    anos_passados = idade - 18
    print("Já passou", anos_passados, "anos do prazo de alistamento militar.")
