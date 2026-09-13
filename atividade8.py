nome_do_cliente = input("Digite seu nome: ")
Velocidade_MBPS = float(input("imforme a velocidade contratada em mbps: "))

if Velocidade_MBPS <= 50:
    classificação_do_plano = "plano basico"
elif Velocidade_MBPS <= 199:
    classificação_do_plano = "plano intermediario"
elif Velocidade_MBPS <= 499:
    classificação_do_plano = "plano avançado"
else:
   classificação_do_plano  = "plano ultra"

print(f"cliente: {nome_do_cliente}")
print(f"Velocidae MBPS: {Velocidade_MBPS}")
print(f"classificação_do_plano: {classificação_do_plano}")