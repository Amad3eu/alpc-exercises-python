peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
limite = 50
if peso_peixes > limite:
    excesso = peso_peixes - limite
    multa = excesso * 4
    print(f"O peso excedente é de {excesso:.2f} quilos.")
    print(f"O valor da multa a ser pago é de R$ {multa:.2f}.")
else:
    print("Não há excesso de peso.")
