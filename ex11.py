import math

largura = float(input('Digite a largura da parede a ser pintada: '))
altura = float(input('Digite a altura da parede a ser pintada: '))
area = largura * altura
tinta = math.ceil(area / 2)
print(f'A área a ser pintada é de {area:.2f} m² e serão necessários {tinta} litros de tinta para pinta-la.')