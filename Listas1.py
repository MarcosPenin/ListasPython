"""Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
 y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo."""
import random

print("LISTA, CUADRADO Y CUBO")

lista = []
contador=0
for i in range(0,10):
    n = random.randint(1,10)
    lista.append(n)
    contador+=1
    print("Número",contador,"=",n,"Cuadrado=",n*n,"Cubo=",n*n*n)

