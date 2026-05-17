est = int(input('Quantas horas você ficou no estavionamento? '))
horas = 5*est

if horas >= 35:
    print(f'O valor a ser cobrado por {est} horas é de 35,00R$')
if  horas < 35:
    print(f'O valor a ser cobrado por {est} horas é de {horas}')