livros = []

opcao = 0

while opcao != 3:

    print("\n===== MENU =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        quantidade = int(input("\nQuantos livros deseja cadastrar? "))

        contador = 1

        while contador <= quantidade:

            print("\n--- CADASTRO DO LIVRO", contador, "---")

            titulo = input("Digite o nome do livro: ")
            autor = input("Digite o autor: ")
            ano = input("Digite o ano de publicação: ")

            livro = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano
            }

            livros.append(livro)

            print("\nLivro cadastrado com sucesso!")

            contador = contador + 1

        print("\nCadastro finalizado!")

    elif opcao == 2:

        print("\n===== LISTA DE LIVROS =====")

        if len(livros) == 0:
            print("Nenhum livro cadastrado.")

        else:
            contador = 1

            while contador <= len(livros):

                livro = livros[contador - 1]

                print("\nLivro", contador)
                print("Nome:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])

                contador = contador + 1

    elif opcao == 3:

        print("\nSaindo do programa...")

    else:

        print("\nOpção inválida! Tente novamente.")