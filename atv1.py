
valor_casa = float(input('\nInforme o valor do imovel: '))
salario = float(input('Informe o salário: '))
anos = int(input('Informe em quantos anos será pago: '))

quant_prest = anos * 12
prest_mensal = valor_casa/quant_prest

if salario * 0.3 > prest_mensal:
    print('\n\nSeu empréstimo bancário foi aprovado!!')
    print('Você pagará {} prestações de R${:.2f} por {} anos'.format(quant_prest, prest_mensal, anos))

else:
    print('Infelizmente você não foi aprovado para o empréstimo, sentimos muito.')