par = []
impar =[]

for i in range (1,11):
    v1 = int(input(f'Digite número {i}: '))

    if v1 % 2 ==0:
        par.append(v1)
    else:
        impar.append(v1)
print(f'os números pares que você digitou foram: {par}')
print(f'os números impares que você digitou foram: {impar}')