'''
En una escuela, luego de tomar un determinado examen, es necesario calcular 
el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. 
Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8),
aceptable (el promedio está comprendido entre 6 y 8)
o bajo (promedio es inferior a 6). 
Desarrollar un algoritmo que resuelva este problema.
Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes
del curso han rendido el examen.
'''

#Preguntar la cantidad de alumnos que han rendido
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que han rendido el examen: "))
notas = []
#Ingresar las notas logradas por los alumnos
for i in range (cantidad_alumnos):
    nota = float(input("Ingrese las notas logradas por los alumnos: "))
    notas.append(nota)

#Calcular promedio
promedio = sum(notas) / len(notas)

#Imprimir tipo promedio
if promedio < 6:
    print ("El promedio tennido es bajo")

if 5 < promedio < 9:
    print ("El promedio tennido es aceptable")

if promedio > 8:
    print ("El promedio tennido es bajo")

print (f"promedio{promedio:.2f}")

