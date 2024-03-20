area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 3  # 3 metros quadrados por litro
litros_necessarios = area_pintada / cobertura_por_litro
print(litros_necessarios)
print(litros_necessarios % 18)
latas = int(litros_necessarios / 18) + (1 if litros_necessarios % 18 != 0 else 0)
preco_total = latas * 80
print(f"Você precisará de {latas} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")
