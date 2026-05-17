titulo = 'Estrutura de repeticao while - tabuada'
print(f'{titulo:^60}')

resp = 's'
n = int(input('Digite o número para ser feito sua tabuada: '))

while resp == 's':
    i = 1
    while i <= 10:
        tabuada = n * i
        print(f'{n}X{i}={tabuada}')
        i = i + 1
    resp = input('Você gostaria de calcular a próxima tabuada?')
    if resp == 's':
        n = n + 1