titulo = 'Saudavel'
print(f'{titulo:^40}')

verduras = input('Você come verduras todos os dias? ') . lower()
exercicios =  input('Você faz exercicios ao menos três vezes na semana? ') .lower()

if verduras in ( 'sim','yes') or exercicios in ('sim', 'yes'):
    print('Você é saudavel! ')
else:
    print('Você precisa melhorar... ')