def temperature(temp):
    if temp > 20:
        return "Está calor!"
    else:
        return "Está frio!"

temp = float(input("Digite a temperatura atual: "))
print(temperature(temp))