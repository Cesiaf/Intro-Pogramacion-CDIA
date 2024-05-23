// Declarar variable
nombre <- cadena

// Inicializar un bucle infinito
Mientras Verdadero Hacer
    //Solicitar un nombre
    Escribir "Ingrese un nombre, para finalizar la lista ingrese FIN: "
    Leer nombre 
    nombre <- ConvertirAMinusculas(nombre)

    // Mostrar el nombre ingresado
    Escribir nombre

    //Verificar si el nombre ingresado es "fin"
    Si nombre = "fin" Entonces
        // Salir del bucle si el nombre es "fin"
        Romper
    FinSi
SinMientras
