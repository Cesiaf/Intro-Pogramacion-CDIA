'''
EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared.

'''

#Solicitar al usuario que ingrese las dimensiones de la obra
largo = float(input("Ingrese el largo de la pared en metros: "))
ancho = float (input("Ingrese el ancho de la pared en metros: "))

#Solicitar al usuario que ingrese el costo por metro cuadrado
costo_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado: "))

#Calcular el área de la pared
area_pared = largo * ancho

#Calcular el costo total de la mano de obra.
costo_total = area_pared * costo_metro_cuadrado

#Imprimir el costo total de la mano de obra.
print(f"El costo total para pintar la pared es: ${costo_total:.2f}")