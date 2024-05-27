Algoritmo lista_nombres

	// Declarar variable
	Definir nombre como cadena
	Definir continuar como logico // Esta variable se utilizará como condición de salida del bucle
	
	continuar <- Verdadero // Inicializamos la variable en Verdadero para comenzar el bucle
	
	// Inicializar un bucle
	Mientras continuar Hacer
		// Solicitar un nombre
		Escribir "Ingrese un nombre, para finalizar la lista ingrese FIN: "
		Leer nombre 
		nombre <- minusculas(nombre)
		
		// Mostrar el nombre ingresado
		Escribir nombre
		
		// Verificar si el nombre ingresado es "fin"
		Si nombre = "fin" Entonces
			// Cambiar la condición de salida del bucle
			continuar <- Falso
		FinSi
	FinMientras
FinAlgoritmo