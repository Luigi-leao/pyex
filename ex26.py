contagem = str(input("Digite uma frase para contar os 'a': ")).lower().strip()
print ("A letra 'a' aparece {} vezes".format(contagem.count('a')))
print ("A letra 'a' aparece pela primeira vez na posição: {}".format(contagem.find('a')+1))
print ("A letra 'a' aparece pela ultima vez na posição: {}".format(contagem.rfind('a')+1))
