"""
Actividad 1: Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número.
Actividad 2: Escribe el código de un ciclo para obtener el número de dígitos de un número ingresado por el usuario.
Actividad 3: Escribe el código que solicite números al usuario hasta que éste ingrese -1. Cuando se ingrese -1, 
el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
"""
def actividad1():
    i=2
    print("actividad1")
    inicial = int(input("Ingrese el numero"))
    if inicial % 2 == 0:
        while i<inicial:  
            i % 2 == 0
            print(i)    
            i+=2   
    else:
        print("el numero no es primo ")
            
def actividad2():
    print("actividad2")
    numero = input("Ingrese el numero a verificar")
    indice = 0
    while indice < len(numero):
        letra = numero[indice]
        indice += 1

    print(f"El numero a verificar tiene {indice} digitos")
    #Escribe el código de un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

def actividad3():
    print("actividad3")
    i=0
    cont=1
    suma=0
    var=0
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
    while True:
        var = int(input(f"Escribe el numero en la posición {cont} "))
        if var != -1:
            suma+=var
        else:
            break
        cont+=1
    i=suma/(cont-1)
    print(f"El promedio de los {cont} ingresados es: {i}")


if __name__ == "__main__":

    actividad1()
    actividad2()
    actividad3()