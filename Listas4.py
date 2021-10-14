"""Diseñar el algoritmo correspondiente a un programa, que:  Crea una tabla (lista con dos dimensiones) de 5x5 enteros. 
 Carga la tabla con valores numéricos enteros. 
 Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla"""

import random

print("TABLA CON LAS FILAS Y LAS COLUMNAS SUMADAS")

lista1,lista2,lista3,lista4,lista5=[],[],[],[],[]

for i in range(0,5):
    n = random.randint(0,20)
    lista1.append(n)
    n = random.randint(0,20)
    lista2.append(n)
    n = random.randint(0,20)
    lista3.append(n)
    n = random.randint(0,20)
    lista4.append(n)
    n = random.randint(0,20)
    lista5.append(n)

tabla=lista1,lista2,lista3,lista4,lista5

sumaColumna1=sumaColumna2=sumaColumna3=sumaColumna4=sumaColumna5=0

for row in tabla:   
    sumaColumna1+=row[0]
    sumaColumna2+=row[1]
    sumaColumna3+=row[2]
    sumaColumna4+=row[3]
    sumaColumna5+=row[4]

sumaFila1=sum(tabla[0])
sumaFila2=sum(tabla[1])
sumaFila3=sum(tabla[2])
sumaFila4=sum(tabla[3])
sumaFila5=sum(tabla[4])

print(lista1,"|",sumaFila1)
print(lista2,"|",sumaFila2)
print(lista3,"|",sumaFila3)
print(lista4,"|",sumaFila4)
print(lista5,"|",sumaFila5)
print("-------------------------")

print(sumaColumna1,sumaColumna2,sumaColumna3,sumaColumna4,sumaColumna5)

