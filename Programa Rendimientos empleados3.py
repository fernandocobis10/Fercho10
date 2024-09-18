# Programa para evaluar el rendimiento de los empleados y calcular el salario

# Leer la puntuación del usuario
puntuacion = int(input("Introduce tu puntuación (0, 4, 6 o más): "))

# Definir el salario base
salario_base = 2400

# Determinar el nivel de rendimiento y calcular el salario
if puntuacion == 0:
    rendimiento = "Inaceptable"
    salario = salario_base * puntuacion // 10
elif puntuacion == 4:
    rendimiento = "Aceptable"
    salario = salario_base * puntuacion // 10
elif puntuacion >= 6:
    rendimiento = "Meritorio"
    salario = salario_base * puntuacion // 10
else:
    rendimiento = "Puntuación no válida"
    salario = 0

# Mostrar el resultado
print(f"Tu nivel de rendimiento es: {rendimiento}")
print(f"Te corresponde cobrar: ${salario}")
