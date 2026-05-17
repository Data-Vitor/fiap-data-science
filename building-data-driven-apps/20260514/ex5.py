import random

numeros = []

# Preencher a lista com 10 números aleatórios
for i in range(10):
    numero = random.randint(1, 6)  # diminui o range para aumentar a chance de repetidos
    numeros.append(numero)

numero = int(input('Entre com um numero de 1 a 6: '))
print(f'O numero {numero} aparece {numeros.count(numero)} vezes')