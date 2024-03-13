n = 0
soma = 0
while(n >= 0):
    print('[finalizar = num negativo]')
    n = float(input('digite um numero:  ')) 
    if (n % 2== 0) and (n > 0):
        soma = soma + n
        print(f'a soma dos numero pares é {soma}')
        print('')
    elif(n % 2 != 0) and (n > 0):
        print(f'O Numero {n} é impar')
        print('')
    else:
        print('')
        