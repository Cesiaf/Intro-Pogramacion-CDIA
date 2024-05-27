# 1. Condicional parcial (solo el if) con expresión lógica simple

numero = int(input("Ingrese un número: "))

# Situación: Un programa que verifica si un número es positivo.

if numero > 0:
    print("El núemero es positivo: ")

#2. Condicional completo (if - else) con expresión lógica simple
#Situación: Un programa que indica si un número es par o impar.

if numero % 2 == 0:
    print("El núemero es par")
else:
    print("El núemero es impar")

#3. Condicional parcial (solo el if) con expresión lógica compuesta (and)
#Situación: Un programa que verifica si un número está en el rango de 10 a 20.

if 10 <= numero <= 20:
    print("El núemero está en el rango de 10 a 20")

#4. Condicional completo (if - else) con expresión lógica compuesta (or)
#Situación: Un programa que verifica si un número es múltiplo de 3 o de 5.

if numero % 3 == 0 and numero % 5 == 0:
    print("El núemero es múltiplo de 3 y de 5")
else: 
    print("El núemero no es múltiplo de 3 y ni de 5")