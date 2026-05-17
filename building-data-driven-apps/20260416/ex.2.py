# Seu Nome Aqui

# Parte 1 - Cadastro de Usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"\033[36m\nBem-vindo(a), {nome}! Você tem {idade} anos. Bom empréstimo!\033[0m")

# Parte 2 - Empréstimo de Livros
romance = 0
aventura = 0
historia = 0

while True:
    total = romance + aventura + historia

    if total >= 5:
        print("Máximo de 5 livros atingido!")
        break

    print("\n=== MENU DE LIVROS ===")
    print("1 - Romance")
    print("2 - Aventura")
    print("3 - História")
    print("4 - Encerrar empréstimos")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            romance += 1
            print("Livro de Romance emprestado!")

        case "2":
            aventura += 1
            print("Livro de Aventura emprestado!")

        case "3":
            historia += 1
            print("Livro de História emprestado!")

        case "4":
            print("Encerrando empréstimos...")
            break

        case _:
            print("Opção inválida!")

# Parte 3 - Relatório de Empréstimos
total = romance + aventura + historia

print("\n==============================")
print("   RELATÓRIO DE EMPRÉSTIMOS   ")
print("==============================")
print(f"Usuário  : {nome}")
print(f"Romance  : {romance}")
print(f"Aventura : {aventura}")
print(f"História : {historia}")
print(f"Total    : {total}")
print("==============================")

# Parte 4 - Cadastro da Data de Entrega
for i in range(1, total + 1):
    data = input(f"\nDigite a data de entrega do livro {i}: ")
    print(f"Data do livro {i} registrada: {data}")