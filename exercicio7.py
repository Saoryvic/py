def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total


print("===== BIBLIOTECA ===== \n")
print("1 - Calcular total \n")
print("2 - Sair \n")

opcao = int(input("Escolha uma opção: \n"))
quantidade_livros = int(input("Quantidade de livros :\n "))

for i in range (1, quantidade_livros +1):

    livro = input(f"\nPor favor, incira o nome do livro: {quantidade_livros} \n")
    if opcao == 1:
        
        preco = float(input(" Insira o preço do livro: \nR$ "))
        quantidade = int(input("Insira a quantidade: "))

        resultado = calcular_total(preco, quantidade)

        print("O resutado final é: R$", resultado)

    elif opcao == 2:
        print("Programa encerrado.")
        break

else:
     print("Usuario, sua opção está invalida ...")