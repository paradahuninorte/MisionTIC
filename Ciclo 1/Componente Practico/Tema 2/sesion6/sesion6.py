# Diseñar 3 funciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e informar si es par o impar. #!SOLUCIONADO!
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número con el mayor del primero y el menor del segundo. #!SOLUCIONADO!
#   3. Leer un número de 3 dígitos y formar el mayor número posible con sus cifras.#!SOLUCIONADO
#
# Crea la función principal como un menú con las tres opciones.

def menu():
    while True:
        decision = int(input("**** Hola! ingrese en el menú, la opción que quiere realizar ****\n1.Mostrar mayor par/impar\n2.seleccione el mayor de los dos numeros\n3.Ordenar por mayor\n4.Salir\n"))
        if decision == 1:
            funcion1()
        if decision == 2:
            funcion2()
        if decision == 3:
            funcion3()
        if decision == 4:
            break

def funcion1():
    numeros=[]
    i=0
    for i in range(4):
        num = float(input("Ingerse el numero #{}: ".format(i+1))) #captura los numeros
        numeros.append(num) #*Append agrega los # al array
    mayor = numeros[0] #*Se le asigna como mayor al primer valor de la lista
    for numero in numeros: #se recorre la lista | for <elem> in <iterable>:
        if numero > mayor:
            mayor = numero
    if mayor % 2 == 0:
        print("El digito Mayor es: ",mayor,", y el numero es par")
    else:
        print("El digito Mayor es: ",mayor,", y el numero es impar")

def funcion2():
    numeros=[]
    i=0
    for i in range(3):#3 digitos, cuenta de 0 a 3
        num = float(input("Ingerse el numero #{}: ".format(i+1))) #captura los numeros
        numeros.append(num) #*Append agrega los # al array
    mayor = numeros[0] #*Se le asigna como mayor al primer valor de la lista
    menor = numeros[0] #*Se le asigna como mayor al primer valor de la lista
    for numero in numeros: #se recorre la lista | for <contador> in <coleccion>:
        if numero > mayor:
            mayor = numero
    for numero in numeros: #se recorre la lista | for <contador> in <coleccion>:
        if numero < menor:
            menor = numero
    print(f"El numero mayor es {mayor}, el numero menor es {menor} y juntos son: %i%i" % (mayor,menor))

def funcion3():
    numeros=[]
    ordenados=[]
    i=0
    for i in range(3):#3 digitos, cuenta de 0 a 3
        num = float(input("Ingerse el numero #{}: ".format(i+1))) #captura los numeros
        numeros.append(num) #*Append agrega los # al array
    ordenados = sorted(numeros, reverse=True)
    print("El mayor numero posible es %i%i%i" % (ordenados[0],ordenados[1],ordenados[2]))

if __name__ == "__main__":
    menu()

