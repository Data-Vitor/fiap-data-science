nomes = []
idade = []
aprovados = []
for i in range (1,5):
    v1 = (input(f'Digite o nome da pessoa numero: {i}: '))
    v2 = (int(input(f'Digite a idade da pessoa numero: {i}: ')))
    nomes.append(v1)
    idade.append(v2)
    if v2 >= 18  :
        aprovados.append(v1)
print(aprovados)
