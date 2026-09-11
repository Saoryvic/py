produto = input("digite o nome do produto: ")
Quantidade_disponivel = int(input("Informe a quantidade de produto disponível: "))

if Quantidade_disponivel == 0:
    situação = "Produto esgotado"
elif Quantidade_disponivel <= 5:
    situação = "Estoque critico"
elif Quantidade_disponivel <= 20:
    situação = "Estoque baixo"
else:
    situação = "Estoque normal"

print(f"nome do produto: {produto}")
print(f"quantidade disponivel: {Quantidade_disponivel}")
print(f"estoque: {situação}")