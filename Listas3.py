"""Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que
 introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se 
 introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:  Todos los alumnos mayores de edad.  
 Los alumnos mayores (los que tienen más edad)"""

print("ALUMNOS POR EDADES")

nombre=""
listaAlumnos=[]
edadMaxima=0

while(nombre!="*"):   
   nombre=(input("Introduce el nombre del alumno:"))
   if nombre!="*":
    alumno=[]
    edad=(int(input("Introduce la edad del alumno:")))
    alumno.append(nombre)
    alumno.append(edad)
    listaAlumnos.append(alumno)
    if edad>edadMaxima:
        edadMaxima=edad

print("Alumnos mayores de edad:")
for [n,m] in listaAlumnos:
    if m>17:
        print("Nombre:",n,"Edad:",m)
    
print("Alumnos con la mayor edad:")
for[n,m] in listaAlumnos:
    if m==edadMaxima:
       print("Nombre:",n,"Edad:",m) 

