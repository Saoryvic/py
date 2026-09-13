print("================================")
print("sistema para biblioteca")
print("================================")
Acessos = (input("Quantas vezes deseja acessar o sistema? "))

print("1- Cadastrar livro:")
print("2- Cadastrar aluno:")
print("3- Ralizar emprestimo:")
print("4- Sair...")

opçao = input("Escolha uma das opçoes: ")

if opçao == "1":
    quantidade_livros = int(input("Quantos livrsos deseja cadastra?"))

    for i in range (quantidade_livros ):
        print("LIVRO")
        Codigo = input("Codigo:")

titulo = input("titulo:")
if titulo == "":
    print("titulo do livro: ")

autor = input("autor: ")
if autor == "":
    print("autor do livro: ")

ano = int(input("ANO: "))
if ano <=0:
    print("ano invalido! ")

    quantidade = int(input("quantidade: "))
    if quantidade <=0:
        print(" Sua quantidae de livros deve ser maior que 0: ")

    else:
        print("Seu livro foi cadastrado com sucesso!")

elif opçao == "2":
    quantidade_alunos = int(input("Quantos alunos deseja cadastrar?"))
    for i in range(quantidade_alunos):
        print("ALUNO")
        matricula = input("matricula: ")
        if matricula == "":
            print("matricula do aluno: ")

        nome = input("nome: ")
        if nome == "":
            print("nome do aluno: ")

        idade = int(input("idade: "))
        if idade <=0:
            print("idade invalida! ")

        else:
            print("Seu aluno foi cadastrado com sucesso!")

elif opçao == "3":
    print("Realizar emprestimo")

    codigo_livro = input("Codigo do livro: ")
    if codigo_livro == "":
        print("Codigo do livro: ")

    else:
        matricula_aluno = input("Matricula do aluno: ")
        if matricula_aluno == "":
            print("Matricula do aluno: ")

        else:
            quantidade_emprestimo = int(input("Quantidade de livros a emprestar: "))
            if quantidade_emprestimo >0:
                print("Emprestimo realizado com sucesso!")

            else:
                print("Nao é possivel realizar emprestimos com quantidade menor ou igual a 0!") 
                print("Emprestimo nao realizado!")

elif opçao == "4":

    print("Saindo do sistema...") 
    print("Sistema encerrado!")

else:

    print("Opção invalida! Tente novamente :( ... ")