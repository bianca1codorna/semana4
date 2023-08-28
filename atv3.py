from datetime import date

ano = int(input('\nInforme o ano de seu nascimento: '))
calc_idade = date.today().year - ano

if calc_idade < 18:
    print('\nVocê ainda não precisa se alistar nas forças armadas, em {} anos você deverá se alistar.'.format(18 - calc_idade))
elif calc_idade == 18:
    print('\nVocê deve se apresentar na junta mais próxima antes de Junho.')
else:
    print('\nVocê já passou do tempo de alistamento em {} anos, se apresente na junta mais próxima para mais informações.'.format(calc_idade - 18))