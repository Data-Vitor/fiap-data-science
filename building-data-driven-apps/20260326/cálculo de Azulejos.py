#Vitor Matias do Nascimento - RM572761


comp = int(input('Digite o comprimento do banheiro em metros: '))
larg = int(input('Digite a largura do banheiro em metros: '))
alt = int(input('Digite a altura do banheiro em metros: '))
azullarg = int(input('Digite a largura do azulejo desejado em centimetros: '))
azulalt = int(input('Digite a altura do azulejo desejado em centimetros: ' ))

areatotal = (2 * comp * alt) + (2 * larg * alt)

areaazul = (azullarg /100) * (azulalt /100)

quantazul = areatotal/areaazul

caixa  =  int( quantazul/10)

print(f'A quantidade de caixas necessárias será de {caixa} caixas.')


