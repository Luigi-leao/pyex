city = str(input("Digite uma cidade que o início do nome dela comece com a palavra 'santo': ")).strip()
print("A cidade começa com 'Santo'? {}".format(city[0:5].lower() == "santo"))
