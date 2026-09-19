print("OLÁ, SEJA BEM VINDO!\n" "POR FAVOR RESPONDA A PERGUNTA ABAIXO. >>>")

quantidade = int(input("\nQUANTOS ALUNOS DESEJA CADASTRAR?  \n"))

Contador = 1
while Contador <= quantidade:
    nome = input("POR FAVOR DIGITE O NOME DO ALUNO: \n")
    print("\nALUNO CADASTRADO NO SISTEMA COM SUCESSO :\n",nome)
    Contador = Contador + 1

print("\nTODOS OS ALUNOS FORAM CADASTRADOS COM SUCESSO")