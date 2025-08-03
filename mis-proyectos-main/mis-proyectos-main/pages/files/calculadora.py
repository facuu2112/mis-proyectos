def suma(x,y):
    return x + y
    
def resta (x,y):
    return x - y
    
def multiplicacion(x,y):
    return x * y
    
def division(x,y):
    return x / y

while True:
    print("selecciona la operacion")
    print("  1. suma")
    print("  2. resta")
    print("  3. multiplicacion")
    print("  4. division")
    operacion = input("selecciona la operacion(1/2/3/4):")

    if operacion in ("1,2,3,4"):
        try:
            num1 = float(input("ingrese un numero"))
            num2 = float(input("ingrese otro numero"))
        except:
            print("error: ingrese un numero")
            continue
        if operacion == "1":
            print(suma(num1,num2))    
        elif operacion == "2":
            print(resta(num1,num2))
        elif operacion == "3":
            print(multiplicacion(num1,num2))
        elif operacion == "4":
            print(division(num1,num2))
    else:
        print("error: Ingrese una opcion correcta")
        
    continuar = input("¿quieres continuar?")

    if continuar in ("no"):
        print("no vemo perri flow")
        break
    if continuar in ("si"):
        continue
    