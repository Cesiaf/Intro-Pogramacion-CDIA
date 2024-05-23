'''
EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada
materia y quiere saber cuál es su promedio.
'''
#Solicitar al usuario que ingrese la cantidad de Materias
materias = int(input("Ingrese la cantidad de Materias: "))

# Solicitar al usuario que ingrese las notas de cada materia
notas = []
for i in range(1, materias+1):
    nota = float(input(f"Ingresa la nota de la materia {i}: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Imprimir el promedio
print(f"El promedio de las notas es: {promedio:.2f}")
