print("...........................................")
print("Bem vindo(a) ao nosso sistema escolar\n")
print("nomes de alguns alunos ja cadastrados: ")
print("...........................................\n")

Lista_Estudantes = [f"\nkayra","mari", "kiara","vanessa\n"]

for contador in Lista_Estudantes:
    print(contador)

#VARIAVEL PARA ADICIONAR ALUNOS
AdicionarEstudantes = int(input("Quantos estudantes seram cadastrados? "))

for i in range (1, AdicionarEstudantes  +1):

    print(f">>>>>> ALUNO <<<<<<< {i}")
    AdicionarEstudantes = input("\nPor favor informe o nome do aluno a ser cadastrado: ")
    Lista_Estudantes.append(AdicionarEstudantes)

    print("\n>>>>>>>> PARABENS SEU CADRASTRO FOI REALIZADO COM SUSECESSO! <<<<<<<<<< \n")

for aluno in Lista_Estudantes:
        print(aluno)
        print("................................\n")