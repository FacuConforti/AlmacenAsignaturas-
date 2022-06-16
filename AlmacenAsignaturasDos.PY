asignaturas = []
notas = []
aprobadas = []
desaprobadas = []
notasAprobadas = []
notasDesaprobadas = []
cont = 0
suma = 0

continuar = input("Desea comenzar a utilizar el programa? SI / NO (en mayusculas) ")

while continuar != "SI" and continuar != "NO":
    continuar = input("Desea comenzar a utilizar el programa? SI / NO (en mayusculas) ")

while continuar == "SI":

    asignatura = input("Ingrese la asignatura que desee agregar" )
    asignaturas.append(asignatura)

    nota = int(input("Ingrese la nota que obtuvo en esta asgintarura" ))
    while nota < 1 or nota > 10:
       nota = int(input("Ingrese la nota que obtuvo en esta asgintarura" ))

    if nota >= 1 and nota <= 6:
        notasDesaprobadas.append(nota)
        desaprobadas.append(asignatura)
    elif nota >= 7 and nota <=10:
        notasAprobadas.append(nota)
        aprobadas.append(asignatura)
        

    notas.append(nota)
    
    suma = suma + nota

    cont = cont + 1

    continuar = input("Desea seguir utilizando el programa? SI / NO (en mayusculas)" )
    while continuar != "SI" and continuar != "NO":
        continuar = input("Desea seguir utilizando el programa? SI / NO (en mayusculas)" ) 
print("Todas las Materias: ")
for i in range(len(asignaturas)):
    print("Asignatura: ", asignaturas[i]," Nota: ", notas[i])

print("Las Materias Aprobadas son: ")
for n in range(len(aprobadas)): 
    print("Asignatura: ", aprobadas[n]," Nota: ", notasAprobadas[n])

print("Las Materias Desaprobadas son: ")
for j in range(len(desaprobadas)): 
    print("Asignatura: ", desaprobadas[j]," Nota: ", notasDesaprobadas[j])

print("El promedio de todas las notas es de: ", (suma/cont))