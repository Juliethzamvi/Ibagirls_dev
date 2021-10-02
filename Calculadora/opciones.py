from menu import *
from Operaciones_basicas.suma import sumar
from Operaciones_basicas.resta import restar
from Operaciones_medio.multiplicacion import multiplicar
from Operaciones_medio.division import dividir

def getOption():
    opt = int(input("Inserte la opcion del menu: "))
    res = 0
    if (opt in (1, 2, 3, 4)):
        num1 = int(input("Inserte el numero 1: "))
        num2 = int(input("Inserte el numero 2: "))
        if(opt == 1):
            res = sumar(num1, num2)
        if(opt == 2):
            res = restar(num1, num2)
        if(opt == 3):
            res = multiplicar(num1, num2)
        if(opt == 4):
            res = dividir(num1, num2)
        print("El resultado de la operacion es: ", res)
        getOption()
    elif(opt == 5):
        exit()
    else:
        print("Opcion no valida! Digite de nuevo")
        menu()
        getOption()

