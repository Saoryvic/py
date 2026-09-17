print("Bem vindo(a) ao nosso sistema escolar\n")
print("nomes de alguns alunos ja cadastrados: \n")

Lista_Estudantes = ["kayra", f"\nmari", f"\nkiara", f"\nvanessa\n"]

for contador in Lista_Estudantes:
    print(contador)

#VARIAVEL PARA ADICIONAR ALUNOS
AdicionarEstudantes = int(input("Quantos estudantes seram cadastrados? "))

for i in range (1, AdicionarEstudantes  +1):

    print(f">>>>>> ALUNO <<<<<<<{i}")
    AdicionarEstudantes = input("\nPor favor informe o nome do aluno a ser cadastrado: ")
    Lista_Estudantes.append(AdicionarEstudantes)

    print("\n>>>>>>>> cadastro atualizado <<<<<<<<<<")

for aluno in Lista_Estudantes:
        print(aluno)