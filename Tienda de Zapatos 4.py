# Programa para calcular el descuento en una tienda de zapatos

# Precio de un zapato 
precio_zapato = 80

# Calcular el número de zapatos comprados
num_zapatos = int(input("Introduce el número de zapatos comprados: "))

# Calcula el total sin descuento
total_sin_descuento = num_zapatos * precio_zapato

# Determinar el descuento basado en la cantidad de zapatos
if num_zapatos > 30:
    descuento = 0.40
elif num_zapatos > 20:
    descuento = 0.20
elif num_zapatos > 10:
    descuento = 0.10
else:
    descuento = 0.0

# Calcular el total con descuento
total_con_descuento = total_sin_descuento * (1 - descuento)

# Mostrar el resultado
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total con descuento: ${total_con_descuento:.2f}")
