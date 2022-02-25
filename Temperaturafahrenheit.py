# Exercício de conversão de temperatura de F° para C°

TempFahrenheit = float(input("Digite uma temperatura Fahrenheit: "))
TempCelsius = (TempFahrenheit - 32) * 5 / 9
print ('A temperatura em Celsius é: {:.2f}'.format(TempCelsius))