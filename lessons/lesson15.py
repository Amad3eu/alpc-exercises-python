area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 6  # 6 metros quadrados por litro
litros_necessarios = area_pintada / cobertura_por_litro

latas_18 = int(litros_necessarios / 18)
litros_restantes = litros_necessarios % 18
galoes_36 = int(litros_restantes / 3.6) + (1 if litros_restantes % 3.6 != 0 else 0)

preco_lata = 80
preco_galao = 25

preco_total_latas = latas_18 * preco_lata
preco_total_galoes = galoes_36 * preco_galao
preco_total_misto = (latas_18 * preco_lata) + (galoes_36 * preco_galao)

print(f"Situação 1: Comprar apenas {latas_18} latas de 18 litros.")
print(f"Preço total: R$ {preco_total_latas:.2f}")

print(f"Situação 2: Comprar apenas {galoes_36} galões de 3,6 litros.")
print(f"Preço total: R$ {preco_total_galoes:.2f}")

print(f"Situação 3: Misturar latas e galões para minimizar o desperdício.")
print(f"Preço total: R$ {preco_total_misto:.2f}")
