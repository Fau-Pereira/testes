# Inicia o programa
print(
    f'''
    ######### Par ou Impar #########
    #                              #
    # Qual número é par ou impar?  #
    #       Vamos descobrir!       #
    #                              #
    ################################
    '''
)
numero = int(input('Digite um número: ')) # Solicita ao usuário um número inteiro

if numero % 2 == 0: # TODO: Verifique se o número é par ou ímpar e imprima o resultado:
    print(f'Par.')
else:
    print(f'Ímpar.')