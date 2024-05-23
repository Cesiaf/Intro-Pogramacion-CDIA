'''
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades), 
el costo tiene un descuento del 10%. Si compra más de 24 unidades, 
el descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, 
se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
'''

# Calcular el costo total de la leche con descuentos
precio_leche = 1000

# Ingresar la cantidad de unidades de leche y si el cliente es jubilado
cantidad_unidades = int(input("Ingrese la cantidad de unidades de leche: "))
es_jubilado = input("¿Es usted jubilado? (sí/no): ").strip().lower()

# Calcular el descuento basado en la cantidad de unidades
if cantidad_unidades > 24:
    descuento = 0.15
elif cantidad_unidades > 12:
    descuento = 0.10
else:
    descuento = 0.0

# Aplicar descuento adicional si el cliente es jubilado
if es_jubilado in ["sí", "si"]:
    descuento += 0.10

# Calcular el costo total con los descuentos aplicados
costo_total = cantidad_unidades * precio_leche
descuento_total = costo_total * descuento
costo_final = costo_total - descuento_total

# Imprimir el costo final
print(f"El costo a pagar es: {costo_final:.2f} pesos.")
