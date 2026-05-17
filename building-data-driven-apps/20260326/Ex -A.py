bloco = int(input('Digite o número do bloco em que você mora: '))

if bloco in (1,2,3,4,5,6,7,8,9,10):
    print('O sindico responsavel pelo seu bloco é o Sr. José')

if bloco in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
    print('O sindico responsavel pelo seu bloco é o Sr. Hamilton ')

if bloco == 0 or bloco >20:
    print('esse número não corresponde a nenhum bloco do condominio')