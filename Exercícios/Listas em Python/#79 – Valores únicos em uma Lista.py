valores = []

while True:#cria a repetição infinita
    n = int(input('Digite um valor: '))#pedir os valores
    if n not in valores:#determinar valores já adicionados
        valores.append(n)#adicionar os valores a lista
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':#determina uma resposta para quebrar a repetição
        break
print('-=' * 30)
valores.sort()#ordena valores em ordem crescente
print(f'Você digitou os valores {valores}')