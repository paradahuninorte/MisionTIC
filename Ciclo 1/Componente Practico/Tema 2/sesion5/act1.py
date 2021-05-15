'''
Actividad 1: Escribe el código que imprima un comando dada la luz del semáforo
Verde = Siga
Amarillo = Precaución
Rojo = Pare

Actividad 2: Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peatón o no (hayPeaton), imprima:
Verde -------- Si hay peatón: Pare, Sino: Siga
Amarillo ----------- Si hay peatón: Pare, Sino: Precaución
Rojo = Pare
'''
luz = str(input("Ingrese la luz del semáforo \n")).upper()
peaton = str(input("Hay peaton? Si o NO \n")).upper()

if luz == "VERDE" and peaton == "SI":
    print("Pare")
elif luz == "VERDE" and peaton == "NO":
    print("Siga")  

elif luz == "AMARILLO" and peaton == "SI":
    print("Pare")
elif luz == "AMARILLO" and peaton == "NO":
    print("Precaución")

if luz == "ROJO":
        print("Pare!")
