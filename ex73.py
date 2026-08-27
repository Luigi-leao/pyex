times = ('corinthians,',"Palmeiras",'santos','cruzeiro','vasco','chapecoense','Fluminense','Botafogo','Flamengo','atlético,','atlético-PR','bahia','EC vitória','coritiba','avaí','ponte preta','atlético-MG')

print(f'times do brasileirão: {times}')
print(f'5 primeiros {times[0:5]}')
print(f'4 ultimos {times[-4:]}')
print(f'Ordem alfabetica: {sorted(times)}')
print(f'O chapecoense está na {times.index("chapecoense")+1} posição')


