nome = input("digite seu nome:")

tipo_de_problema = ("informe o tipo de problema que esta ocorrendo:")
print("1 -  o computador nao esta ligando mesmo conectado a fonte de energia / o aparelho apresenta um barulho muito alto")
print("2 - a maquina esta super aquecendo / o aparelho se emcontra apresentando problema de video")
print("3 - o aparelho apresenta falha ao abrir programas / o aparelho apresenta lentidão em decorrer do uso ")
print("4 - duvida de como acessar determinados sites")

opçao = input("digite a opção correspondente com o seu problema:")

tempo = input("a quanto tempo o aparelho aprenta esse problema? ")

if opçao == "1":
    problema = "equipamento inoperante ou danificado"
    prioridade = "critica"
elif opçao == "2":
    problema = "instabilidade de desenpenho da maquina"
    prioridade = "alta"
elif opçao == "3":
    problema = "falha no funcionamento de programas má otimi"
    prioridade = "media"
else:
    problema = "atualizaçao do cadrastro"
    prioridade = "baixa"

print(f"cliente: {nome}")
print(f"incidente a ser relatado: {problema} relatado em {tempo}")
print(f"prioridade : {prioridade}")