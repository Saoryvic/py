livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - pesquisar livro")
    print("4 - Excluir livro")
    print("5 - quantidade de livros ")
    print("6 - Sair\n")

    opcao = input("Digite uma opção: ")
    
    if opcao == "1":

        quantidade = int(input("\nQuantos livros deseja cadastrar? "))

        for i in range (1, quantidade +1):
            print(f"\n--- CADASTRO DO LIVRO {i}"  "---")
        
            titulo = input("Digite o nome do livro: ")
            autor = input("digite o nome do autor: ")

            livros.append([titulo, autor])
        
        print("\nLivro cadastrado com sucesso!")
        
 
    elif opcao == "2":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")
        encontre_1livro = False

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontre_1livro = True

        if not encontre_1livro:
            print("NENHUM LIVRO ENCONTRADO! VONTANDO AO MENU INICIAL.....")


    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído!")

    elif opcao == "5":
        print (f"numero de livros ja no cadastro: {len(livros)}")

    
    elif opcao == "6":

        print("O PROGRAMA FOI ENCEERADO .. .. .. .. ..")
        break

    else:

        print("POXA.. SUA OPÇÃO É INVALIDA.")