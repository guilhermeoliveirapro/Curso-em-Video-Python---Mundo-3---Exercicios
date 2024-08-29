palavra = ('aprender', 'programar', 'linguagem', 'python')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aáãâeéêiou':
            print(letra, end=' ')
