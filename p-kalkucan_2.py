import math
figuras = ["Cuadrado","Rectangulo","Circulo","Triangulo","Rombo","Poligonos"]

# Pila
# Indice 0 para Identificadores e Indice 1 para el resultado del retorno
inqueue_prcs = [[],[]]

# Variables necesarias para el script
pi = math.pi

# Funciones para las figuras
def cuadrado(l):
    area = l * 2
    return area

def rectangulo(b,h):
    area = b * h
    return area

def circulo(r):
    area = pi * r**2
    return area

def triangulo(l1,l2,l3):
    lados = (l1 + l2 + l3)/2
    area = (lados * (lados - l1) * (lados - l2) * (lados - l3)) * 0.5
    return area

def rombo(dma,dmi):
    area = (dma * dmi)/2
    return area

def poligono(a,ls,l):
    per = ls * l
    area = (per * a)/2
    return area


print(f"Bienvenido a la calculadora de areas".center(75))
print(f" Kalkucan ".center(75,"="))

size = int(input("¿Cuantas operaciones desea agregar?\n")) # Definir la cantidad de operaciones para el ciclo
for i in range(size):
    print("\nEstas son algunas figuras disponibles, seleccione el número correspondiente.")
    
    for j in range(len(figuras)): # Listado figuras disponibles
        print(f"{j+1}) {figuras[j]}")

    while True: # Ciclo permanente siempre y cuando no se seleccione una figura valida
        n = int(input(f"Introduzca el número correspondiente y presione enter.\n"))-1
        if n == 0 or n == 1 or n == 2 or n == 3 or n == 4:
            print(f"Ha seleccionado con exito la figura {figuras[n]}")
            break
        else:
            print(f"Seleccione una figura valida")
            continue

    if n == 0: # 
        lado = float(input("Inserte el lado: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(cuadrado(lado))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 1:
        base = float(input("Inserte el lado: "))
        altura = float(input("Inserte la altura: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(rectangulo(base,altura))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 2:
        radio = float(input("Inserte el radio: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(circulo(radio))
        print(f"Agregando {figuras[n]} al contenedor")
    
    elif n == 3:
        lado1 = float(input(f"Inserte el lado 1: "))
        lado2 = float(input(f"Inserte el lado 2: "))
        lado3 = float(input(f"Inserte el lado 3: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(triangulo(lado1,lado2,lado3))
        print(f"Agregando {figuras[n]} al contenedor")
    
    elif n == 4:
        diag_min = float(input(f"Inserte la diagonal menor: "))
        diag_may = float(input(f"Inserte la diagonal mayor: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(rombo(diag_min,diag_may))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 5:
        lados = int(input("Numero de lados del poligono: "))
        apotema = int(input("Inserte el apotema: "))
        lado = float(input("Inserte el lado: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(poligono(apotema,lados,lado))
        print(f"Agregando {figuras[n]} al contenedor")


while True: # Ejecutando el metodo lifo
    print(f"Operaciones en el contenedor: ")
    
    # Listando operaciones dentro de la pila (LIFO)
    for w in range(len(inqueue_prcs[0])):
        print(f"{w+1}) Container ID: {inqueue_prcs[0][w]}")
    
    # Imprimiendo el ultimo dato en entrar
    print(f"\nEl resultado de {inqueue_prcs[0].pop()} es: {inqueue_prcs[1].pop()}")

    # Si no hay procesos pendientes romper el ciclo
    if len(inqueue_prcs[1]) == 0:
        break
