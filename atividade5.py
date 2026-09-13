soma = 0

for i in range(1,5):
    nota = float(input("digite a sua nota: "))
    soma = soma + nota
media = soma / 4

print(f"a media final é: {media:.2f}")