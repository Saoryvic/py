st_biblioteca = []

def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total

# opcao = input("Digite uma opção: ")
    
# if opcao == "1":
def cadastro_livros():

    quantidade = int(input("\nQuantos livros deseja cadastrar? "))

    for i in range (1, quantidade +1):
        print(f"\n--- CADASTRO DO LIVRO {i}"  "---")
        titulo = input("Digite o nome do livro: ")
        autor = input("digite o nome do autor: ")
        preco = float(input(" Insira o preço do livro: \nR$ "))
        quantidade = int(input("Insira a quantidade: "))
        resultado = calcular_total(preco, quantidade)
        print(f"O resutado final é: R$, {resultado:.2f}")
        livros_st = [titulo, autor, preco, quantidade, resultado]
        st_biblioteca.append(livros_st)

        print("\nLivro cadastrado com sucesso!")

        
    # elif opcao == "2":
def listagem_lv():
    print("Livros armazenados ao nosso sistema: ")
    if not st_biblioteca:
        print("Seu livros nao foi encontrado no nosso sistema.... ")
        return
    for contador, livros_st in enumerate(st_biblioteca,1):
        print(f"Livro na listagem: {contador}")
        print(f"Lista do sistema da bibliotaecva: {livros_st}")
        print(f"Titulo: {livros_st[0]}")
        print(f"Autor: {livros_st[1]}")
        print(f"Preco: {livros_st[2]}")
        print(f"Quantidade: {livros_st[3]}")
        print(f"Resutado de livros em estoque: {livros_st[4]}\n")



def buscar_livros():
    print("BUSCAR LIVRO ")
      
    pesquisa = input("Digite o título que deseja : ")
    procuro = False

    for livro_st in st_biblioteca:
        if pesquisa in livro_st[0].lower():
            print("LIVRO ENCONTRADO COM SUCESSO! ")
            print(f"titulo{livro_st[0]}")
            print(f"autor{livro_st[1]}")
            print(f"quantidade{livro_st[2]}")
            encontrado = True

    if not procuro:
        print("nenhum livro foi encontrado.....")

def remoção_livros():

    print("remover livro:")
    pesquisa_remocao = input("livro a ser removido: ")
    procuro = False
    for livros_st in st_biblioteca:
        if pesquisa_remocao in livros_st[0].remove():
            print("livro apagado!{livro_st[0]}")

    if not procuro:
        print("nenhum livro foi encontrado!")

def menu():

    while True:

        print("\n===== BIBLIOTECA =====")
        print("1 - \nCadastrar livro")
        print("2 - Listar livros")
        print("3 - pesquisar livro")
        print("4 - remoção de livro")
        print("5 - calculo de livros")
        print("6 - Sair\n")

        opcao = input ("escolha a opcao: ")
        if opcao== "1":
            cadastro_livros()
        elif opcao== "2":
            listagem_lv()
        elif opcao== "3":
            buscar_livros()
        elif opcao=="4":
            remoção_livros()

        elif opcao== "5":
            print("\n saindo do programa....")
        else:
            print("opcao escolhida invalida! ")