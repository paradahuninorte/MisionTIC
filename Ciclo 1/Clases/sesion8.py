'''
suma=0
i=0
estudiantes = int(input("Ingrese el numero de estudiantes\n"))
while i<estudiantes: #i menor a estudiantes, se repetirá el ciclo
    nota=float(input(f"Ingrese la nota del estudiante {i+1}\n"))
    suma += nota
    i+=1
prom= suma/estudiantes
print(f"El promedio de notas del primer parcial es {suma/estudiantes:.2f} calculando en el print")
print(f"El promedio de notas del primer parcial es {prom:.2f} imprimiendo variable")
'''

a=0
suma =0
a = int(input("Ingrese un numero, para terminar ingrese 0"))
while (a!=0):
    suma+=a
    a = int(input("Ingrese un numero, para terminar ingrese 0"))
print("El resultado de la suma es"+str(suma))