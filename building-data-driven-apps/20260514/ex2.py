par = []
media = []
for i in range (1,11):
    v1 = int(input(f'Digite  valor valor. número {i}: '))

    media.append(v1)

    if v1 % 2 ==0:
       par.append(v1)


print(f'A soma dos numeros pares é: {sum(par)}')
print(f'A média aritimética é: {sum(media) / 10}')

