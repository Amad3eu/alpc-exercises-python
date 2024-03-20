altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino ou F para feminino): ").upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para homens é:", peso_ideal)
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para mulheres é:", peso_ideal)
else:
    print("Sexo não reconhecido. Digite M para masculino ou F para feminino.")
