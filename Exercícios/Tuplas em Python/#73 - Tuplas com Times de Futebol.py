times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red Bull Bragantino',
         'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Santos', 'Goiás', 'Coritiba',
         'América-MG')

print('Brasileirão Serie A')
print('-' * 20)
print('TABELA:')
print()
for t in times:
    print(t)
print(f'-' * 15)
print(f'O G4 é {times[:4]}')
print(f'O Z4 é {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')