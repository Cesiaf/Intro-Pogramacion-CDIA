//Declarar variables
precio_leche <- 1000
cantidad_unidades <- 0
es_jubilado <- ""
costo_total <- 0.0
descuento_total <- 0.0
costo_final <- 0.0

//Solicitar la cantidad de unidades de precio_leche
Escribir "Ingrese la cantidad de unidades de leche: "
Leer cantidad_unidades

//Solicitar si el cliente es jubilado
Escribir "¿Es usted jubilado? (sí/no)"
Leer es_jubilado
es_jubilado <- ConvertirAMinusculas(es_jubilado)
es_jubilado <- EliminarEspacios(es_jubilado)

//Calcular el descuento basado en la cantidad de unidades
Si cantidad_unidades > 24 Entonces
    descuento <- 0.15
Sino Si cantidad_unidades > 12 Entonces
    descuento <- 0.10
Sino
    descuento <- 0.0
FinSi

//Aplicar descuento adicional si el cliente es jubilado
Si es_jubilado = "si" o es_jubilado = "sí" Entonces
    descuento <- descuento + 0.10
FinSi

//Calcular el costo total con los descuentos aplicados
costo_total <- cantidad_unidades * precio_leche
descuento_total <- costo_total * descuento
costo_final <- costo_total - descuento_total

//Imprimir el costo costo_final
Escribir "El costo a pagar es: ", costo final, " pesos."

