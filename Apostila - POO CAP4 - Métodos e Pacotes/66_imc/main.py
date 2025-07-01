from imc.calculo import calcular_imc

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f}")