titulo = 'Maioridade'
print(f'{titulo:^40}')
habilitacao = input('Você tem habilitação? ').upper()

idade  = int(input('qual a idade que você tem? '))

if idade >= 18 and habilitacao in ('SIM', 'YES'):
    print('Você pode dirigir.')
else:
    print('Você não pode dirigir.')
print('Obrigado por responder a pesquisa')
