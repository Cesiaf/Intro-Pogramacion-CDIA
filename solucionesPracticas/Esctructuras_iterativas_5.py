'''
Un profesor de matemática necesita generar la tabla de multiplicar de un 
número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería 
aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10
'''

#solicitar el número de tabla necesita el usuario
tabla_numero = int(input("Ingrese el número de tabla que desea generar: "))

#Generar lista de números del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Generar tabla de multiplicar
for i in range(10):
    print(f"{tabla_numero} x {numeros[i]} = {tabla_numero*numeros[i]}")
