
temperaturas = []
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas.append(temp)

promedio = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)
dias_superiores = sum(1 for t in temperaturas if t > promedio)

print("Temperatura promedio de la semana:", promedio)
print("Temperatura más alta:", maxima)
print("Temperatura más baja:", minima)
print("Días con temperatura superior al promedio:", dias_superiores)
