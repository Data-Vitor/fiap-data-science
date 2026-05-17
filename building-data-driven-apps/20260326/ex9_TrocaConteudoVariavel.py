'''titulo = 'Troca de variaveis'
print(f'{titulo:^40}')

A = int(input('Entre com um numero: '))
B = int(input('Entre com outro número: '))

print(f'Variavel A:{A} e Variavel B:{B}')

temp = A
A = B
B = temp
print(f'Variavel A:{A} e Variavel B:{B}')'''


titulo = 'Troca de variaveis'
print(f'{titulo:^40}')
n = int(input('Digite um numero inteiro de 3 digitos: '))
print(n)

c = n//100
resto = n%100
d = resto //10
u = resto %10
final = u*100 + d*10 + c

print(final)


