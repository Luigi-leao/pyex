
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def determinar_situacao(media):
    if media < 5.0:
        situacao = "REPROVADO"
    elif media >= 5.0 and media < 7.0:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "APROVADO"
    return situacao

def main():
  
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
   
    media = calcular_media(nota1, nota2)
 
    situacao = determinar_situacao(media)
  
    print("A média do aluno é", media)
    print("o aluno esta:", situacao)
main()
