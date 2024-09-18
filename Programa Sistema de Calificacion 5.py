# Programa para convertir una calificación en una calificación de (letra)

# Leer la calificación del estudiante
calificacion = int(input("Introduce tu calificación (0-100): "))

# Determinar la calificación en letra
if 90 <= calificacion <= 100:
    letra = 'A'
elif 80 <= calificacion < 90:
    letra = 'B'
elif 70 <= calificacion < 80:
    letra = 'C'
elif 60 <= calificacion < 70:
    letra = 'D'
elif 0 <= calificacion < 60:
    letra = 'F'
else:
    letra = 'Calificación no válida'

# Mostrar el resultado
print(f"Tu calificación es: {letra}")
