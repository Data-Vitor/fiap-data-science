p1 = float(input('Digite a nota da primeira prova: '))
p2 = float(input('Digite a nota da segunda prova: '))
p3 = float(input('Digite a nota da terceira prova: '))

media = (p1+p2+p3)/3

if media >= 6:
    print('Parabéns, você foi aprovado.')
else:
    print('Você foi reprovado.')