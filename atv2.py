num = int(input('Informe um número: '))
esc = int(input('Digite 1 para binario, 2 para octal ou 3 para hexadecimal: '))

if esc == 1:
    print('O número {} em binário fica: {}'.format(num, bin(num)))

elif esc == 2:
    print('O número {} em octal fica: {}'.format(num, oct(num)))

elif esc == 3:
    print('O número {} em hexadecimal fica: {}'.format(num, hex(num)))

else:
    print('Você não escolheu nenhuma das opções.')