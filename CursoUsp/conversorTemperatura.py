temperaturaFahrenheit = input("Digite a temperatura em Fahrenheit: ") #input sempre sera str
f = float(temperaturaFahrenheit) #converte o input para float 
temperaturaCelsius = (f - 32) * 5/9
print("A temperatura em graus Celsius é: %.2f" %(temperaturaCelsius)) # %2.f diminui o ponto flutuante para 2 numeros
