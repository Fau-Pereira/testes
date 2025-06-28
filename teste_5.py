collat = int(input("Digite um número: "))
if collat != 0:
    c0 = collat
    etapas = 0
    print(c0)
    while c0 != 1:
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = c0 * 3 + 1
        print(c0)
        etapas += 1
    print("etapas:", etapas)
else:
    print("Número inválido.")