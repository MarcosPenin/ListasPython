"""Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
A continuación, debe mostrar: todas las notas, la nota media, la nota más alta que ha sacado y la menor."""

import statistics

print("LISTADO NOTAS")


notas=[]
notas.append(float(input("Introduce la primera nota:")))
notas.append(float(input("Introduce la segunda nota:")))
notas.append(float(input("Introduce la tercera nota:")))
notas.append(float(input("Introduce la cuarta nota:")))
notas.append(float(input("Introduce la quinta nota:")))

print("Notas:",notas,"Media:",statistics.mean(notas),"Mejor nota:",max(notas),"Peor nota:", min(notas))





