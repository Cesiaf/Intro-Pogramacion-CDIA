'''EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos'''

#Ingresar cantidad de partidos perdidos
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
                        
#Ingresar cantidad de partidos empatados
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))

#Ingresar cantidad de partidos ganados
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))

#Calcular cantidad de Puntos
cantidad_puntos = partidos_empatados + partidos_ganados*3

#Imprimir cantidad de Puntos
print(f"La cantidad Total que lleva acumulado el equipo es: {cantidad_puntos}")
