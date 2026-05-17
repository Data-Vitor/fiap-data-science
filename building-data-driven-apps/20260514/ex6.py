from faker import Faker
#inicializar uma pessoa
pessoa = Faker('pt_BR')
pessoas = []
for _ in range(10):
    pessoas.append(pessoa.name())

for nome in pessoas:
    print(nome)