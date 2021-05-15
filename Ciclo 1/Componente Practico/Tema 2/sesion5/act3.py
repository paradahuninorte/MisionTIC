'''
Actividad 3: Escribe el código para dos números a y b, el usuario va a seleccionar una opción:
1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y retornar el resultado de la operación indicada.
'''
num1 = 0
num2 = 0
op = 0
num1 = int(input("Ingrese el numero 1 (A)"))
num2 = int(input("Ingrese el numero 2 (B)"))
sel = int(input("1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b)"))

if sel == 1:
    op=num1+num2
    print(f"El resultado de la suma de {num1} más {num2} es {op}")
elif sel == 2:
    op=num1*num2
    print(f"El resultado de la  multiplicación de {num1} por {num2} es {op}")
elif sel == 3:
    op=num1-num2
    print(f"El resultado de la resta de {num1} menos {num2} es {op}")
elif sel == 4:
    op=num1/num2
    print(f"El resultado de la división de {num1} entre {num2} es {op}")