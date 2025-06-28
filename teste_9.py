def verificador_ano_bissexto():
    ano = int(input())
    # TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NAO")

verificador_ano_bissexto()