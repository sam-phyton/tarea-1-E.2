"""
IMC
crea una calculadora de indice de masa corporal"""

weight = float(input("peso en kg: "))
height = float(input("altura en m: "))

imc = weight/ (height ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("peso bajo :(")
elif 18.5 <= imc < 24.9:
    print("peso normal :)")
elif 25 <= imc < 29.9:
    print("sobrepeso :v")
else:
    print("obesidad X(")
    