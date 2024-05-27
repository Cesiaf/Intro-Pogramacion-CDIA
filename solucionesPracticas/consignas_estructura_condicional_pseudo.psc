// Condicional Parcial (solo el if) expresion lógica simple 
// Situación: Un programa que verifica si un número es positivo

Algoritmo Verificar_Positivo

    Definir numero como Entero

    Escribir "Ingrese un número:"
    Leer numero

    Si numero > 0 Entonces
        Escribir "El número es positivo."
    FinSi

FinAlgoritmo

//2. Condicional completo (if - else) con expresión lógica simple
//Situacion: Un programa que indica si un número es par o impar

Algoritmo Verificar_Par_Impar

    Definir numero como Entero

    Escribir "Ingrese un número:"
    Leer numero

    Si numero MOD 2 = 0 Entonces
        Escribir "El número es par."
    Sino
        Escribir "El número es impar."
    FinSi

FinAlgoritmo

//3. Condicional parcial (solo el if) con expresión lógica compuesta (and)
//Situacion: Un programa que verifica si un número está en el rando de 10 a 20, incluyendolos.

Algoritmo Verificar_Rango

    Definir numero como Entero

    Escribir "Ingrese un número:"
    Leer numero

    Si numero >= 10 y numero <= 20 Entonces
        Escribir "El número está en el rango de 10 a 20."
    FinSi

FinAlgoritmo

// 4. Condicional completo (if - else) con expresión lógica compuesta (or)
//Situación:Un programa que verifica si un número es múltiplo de 3 o de 5

Algoritmo Verificar_Multiplo

    Definir numero como Entero

    Escribir "Ingrese un número:"
    Leer numero

    Si numero MOD 3 = 0 o numero MOD 5 = 0 Entonces
        Escribir "El número es múltiplo de 3 o de 5."
    Sino
        Escribir "El número no es múltiplo de 3 ni de 5."
    FinSi

FinAlgoritmo
