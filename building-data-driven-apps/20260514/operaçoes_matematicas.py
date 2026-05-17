'''Aplicativo que mostre as opcões de operações matematicas (soma, subtração, multiplicação e divisão; e solicite dois números e faça a operação matemática.'''

'''print('Assinale qual a operação que você gostaria de realizar: ')
op1 = int(input('Para somar digite 1: \n'
               'Para subtrair digite 2: \n'
               'Para multiplicar digite 3: \n'
               'Para Dividir digite 4: \n'
               'Assinale qual a operação que você gostaria de realizar: '))

op2 = int(input('digite o primeiro numero: '))
op3 = int(input('digite o segunfo numero:' ))


if op1 == 1:
    print('A soma desses dois numéros é:', op2 + op3)
elif op1 == 2:
    print('A subtração desses diois números é:', op2-op3)
elif op1 ==3:
    print('A multiplicação desses dois números é:', op2*op3)
elif op1 ==4:
    if op2 or op3 ==0:
        print('Não é possivel dividir um numero por 0.')
    print('O resultado dessa divisão é:', op2/op3)'''


'''Aplicativo que mostre as opções de operações matematicas (soma, subtração, multiplicação e divisão; e solicite dois números e faça a operação matemática.'''
print('Assinale qual a operação que você gostaria de realizar: ')
op1 = int(input('Para somar digite 1: \n'
                'Para subtrair digite 2: \n'
                'Para multiplicar digite 3: \n'
                'Para Dividir digite 4: \n'
                'Assinale qual a operação que você gostaria de realizar: '))

op2 = int(input('Digite o primeiro numero: '))
op3 = int(input('Digite o segundo numero: '))

if op1 == 1:
    print('A soma desses dois números é:', op2 + op3)
elif op1 == 2:
    print('A subtração desses dois números é:', op2 - op3)
elif op1 == 3:
    print('A multiplicação desses dois números é:', op2 * op3)
elif op1 == 4:
    if op2 == 0 or op3 == 0:
        print('Não é possível dividir um numero por 0.')
    else:
        print('O resultado dessa divisão é:', op2 / op3)
else:
    print('Opção invalida')


