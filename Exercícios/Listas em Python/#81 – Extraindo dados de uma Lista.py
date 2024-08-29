valores = []#lista

while True:#criar uma repetição
    valores.append(int(input('Digite um valor: ')))#ler os valores e adicionar a lista
    r = str(input('Quer continuar ? [S/N]'))
    if r in 'Nn':#determinar a resposta para quebrar a lista
        break#quebrar a repetição
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')#ler quantos valores foram digitados
valores.sort(reverse=True)#ordem decrescente dos numeros
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:#ver se o 5 existe na lista
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')