print("sistema para biblioteca")
print("")
Acessos = (input("Quantas vezes deseja acessar o sistema? "))

print("1- Cadastrar livro:")
print("2- Cadastrar aluno:")
print("3- Ralizar emprestimo:")
print("4- Sair...")

opçao = input("Escolha uma das opçoes: ")

if opçao == "1":
    quantidade_livros = int(input("Quantos livrsos deseja cadastra?"))

for i in range(quantidade_livros):
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