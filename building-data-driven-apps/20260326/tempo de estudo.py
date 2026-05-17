#Vitor Matias do Nascimento RM572761


domingo = int(input('Quantas horas você estudou no domingo? '))
segunda = int(input('Quantas horas você estudou na segunda? '))
terca = int(input('Quantas horas você estudou na terça? '))
quarta = int(input('Quantas horas você estudou na quarta? '))
quinta = int(input('Quantas horas você estudou na quinta? ' ))
sexta = int(input('Quantas horas você estudou na sexta? '))
sabado = int(input('Quantas horas você estudou no sabado? '))

totalsemana = domingo + segunda + terca + quarta + quinta + sexta + sabado

mediadia = totalsemana/7
totalmes = totalsemana*4
totalano = totalsemana*52
totalsemamin = totalsemana *60

print(f'Você estudou {totalsemana} horas essa semana.')
print(f'Você estudou em média {mediadia} horas por dia')
print(f'Você estudou {totalmes} horas esse mes')
print(f'Se manter esse ritmo você estudará {totalano} horas anualmente ')
print(f'Em minutos você estudou {totalsemamin} minutos')