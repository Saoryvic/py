print("================================")
print("sistema para biblioteca")
print("================================")

acessos = int(input("Quantas vezes deseja acessar o sistema? "))

for a in range(acessos):
    print(f"\n--- ACESSO {a + 1} DE {acessos} ---")
    print("1- Cadastrar livro:")
    print("2- Cadastrar aluno:")
    print("3- Realizar emprestimo:")
    print("4- Sair...")
    print("--------------------------------")

    opcao = input("Escolha uma das opçoes: ")

    if opcao == "1":
        quantidade_livros = int(input("\nQuantos livros deseja cadastrar? "))

        for i in range(quantidade_livros):
            print(f"\n--- LIVRO {i + 1} ---")
            
            codigo = input("Codigo: ")

            titulo = input("Titulo: ")
            if titulo == "":
                print("Titulo do livro nao pode ser vazio!")
            else:
                autor = input("Autor: ")
                if autor == "":
                    print("Autor do livro nao pode ser vazio!")
                else:
                    ano = int(input("Ano: "))
                    if ano <= 0:
                        print("Ano invalido!")
                    else:
                        quantidade = int(input("Quantidade: "))
                        if quantidade <= 0:
                            print("Sua quantidade de livros deve ser maior que 0!")
                        else:
                            print("Seu livro foi cadastrado com sucesso!")

    elif opcao == "2":
        quantidade_alunos = int(input("\nQuantos alunos deseja cadastrar? "))
        
        for i in range(quantidade_alunos):
            print(f"\n--- ALUNO {i + 1} ---")
            
            matricula = input("Matricula: ")
            if matricula == "":
                print("\n---Matricula do aluno nao pode ser vazia!")
            else:
                nome = input("Nome: ")
                if nome == "":
                    print("Nome do aluno nao pode ser vazio!")
                else:
                    idade = int(input("Idade: "))
                    if idade <= 0:
                        print("Idade invalida!")
                    else:
                        print("Seu aluno foi cadastrado com sucesso!")

    elif opcao == "3":
        print("\n--- REALIZAR EMPRESTIMO ---")

        codigo_livro = input("Codigo do livro: ")
        if codigo_livro == "":
            print("Codigo do livro nao pode ser vazio!")
        else:
            matricula_aluno = input("Matricula do aluno: ")
            if matricula_aluno == "":
                print("Matricula do aluno nao pode ser vazia!")
            else:
                quantidade_emprestimo = int(input("Quantidade de livros a emprestar: "))
                if quantidade_emprestimo > 0:
                    print("Emprestimo realizado com sucesso!")
                else:
                    print("Nao é possivel realizar emprestimos com quantidade menor ou igual a 0!")
                    print("Emprestimo nao realizado!")

    elif opcao == "4":
        print("\nSaindo do sistema...")
        print("Sistema encerrado!")
        break

    else:
        print("\nOpçao invalida! Tente novamente...")
    
    