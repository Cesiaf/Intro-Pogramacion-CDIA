// Declarar variables
costo_metro_cuadrado <- float
area_pared <- float
largo <- float
ancho <- float
costo_total <- float

// Solicitar dimensiones de la obra
Escribir "Ingrese le largo de la pared en metros: "
Leer largo
Escribir "Ingrese el ancho de la pared"
Leer ancho

// Solicitar costo por metro costo_metro_cuadrado
Leer costo_metro_cuadrado

// Calcular el área de la pared
area_pared = largo * ancho

// Calcular el costo total de la mano de obra
costo_total = area_pared * costo_metro_cuadrado

// Imprimir el costo totall de la mano de obra
Escribir "El costo total para pintar la pared es: $", costo_total
