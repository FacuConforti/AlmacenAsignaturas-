'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.'''
'''IMPLEMENTO: Se le agrego otro vector que almacena notas'''
'''IMPLEMENTO: Se le agrego un contador para sacar el promedio'''

#Asignaturas es el vector que almacena todo
#Asignatura es la variable que se usa para almacenar todo en el vector
#Continuar es la variable que se usa para saber si quiere seguir agregando asignaturas
#Notas es el vector que almacena las notas
#Nota es la variable que se utiliza para almacenar en notas
#Cont va a ser el contador que se utiliza para sacar el promedio
#Suma va a ser la variable que almacena la suma total de las notas
asignaturas = []
notas = []
cont = 0
suma = 0

continuar = input("Desea comenzar a utilizar el programa? SI / NO (en mayusculas)")

while continuar != "SI" and continuar != "NO":
    continuar = input("Desea comenzar a utilizar el programa? SI / NO (en mayusculas)")

while continuar == "SI":

    asignatura = input("Ingrese la asignatura que desee agregar")
    asignaturas.append(asignatura)

    nota = int(input("Ingrese la nota que obtuvo en esta asgintarura"))
    notas.append(nota)
    suma = suma + nota

    cont = cont + 1

    continuar = input("Desea seguir utilizando el programa? SI / NO (en mayusculas)")
    while continuar != "SI" and continuar != "NO":
        continuar = input("Desea seguir utilizando el programa? SI / NO (en mayusculas)")

for i in range(len(asignaturas)):
    print("Asignatura: ", asignaturas[i]," Nota: ", notas[i])

print("El promedio de todas las notas es de: ", (suma/cont))




