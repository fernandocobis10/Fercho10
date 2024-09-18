# Programa para calcular el área de un rectángulo 

# Solicitamos al usuario las dimensiones del rectángulo
base = int(input("Introduce la base del rectángulo: "))
altura = int(input("Introduce la altura del rectángulo: "))

# Calcula el área del rectángulo
area = base * altura

# Muestra el área calculada
print(f"El área del rectángulo es: {area}")

# Verificar las condiciones y mostrar el mensaje personalizado
if area > 40 and altura > 10:
    print("El área es mayor a 40 y la altura es mayor a 10. ¡Buen trabajo!")
