# Program:  Calculadora de Áreas (Return ID from container)
# Method:   Queue (pilas)
# Date:     September 11th, 2022

import math
figuras = ["Cuadrado","Rectangulo","Circulo","Triangulo","Rombo","Poligonos"]

# Pila
# Indice 0 para Identificadores e Indice 1 para el resultado del retorno
instack_prcs = [[],[]]

# Variables necesarias para el script
pi = math.pi
row = 0

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

# Usrer view
print(f"Bienvenido a la calculadora de areas".center(75))
print(f" Kalkucan ".center(75,"="))

size = int(input("¿Cuantas operaciones desea agregar?\t")) # Definir la cantidad de operaciones para el ciclo
for i in range(size):
    print("\n<<< Estas son algunas figuras disponibles, seleccione el número correspondiente.")
    
    for j in range(len(figuras)): # Listado figuras disponibles
        print(f"{j+1}) {figuras[j]}")

    while True: # Ciclo permanente siempre y cuando no se seleccione una figura valida
        row += 1
        print(f"\n· Figura Geometrica {row}")
        n = int(input(f"Introduzca el número correspondiente y presione enter.\t"))-1
        if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
            print(f"\nHa seleccionado con exito la figura {figuras[n]}")
            break
        else:
            print(f"Seleccione una figura valida")
            continue

    if n == 0: # 
        lado = float(input("Inserte el lado:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(cuadrado(lado))
        print(f"Agregando {figuras[n]} al contenedor...")

    elif n == 1:
        base = float(input("Inserte el lado:\t"))
        altura = float(input("Inserte la altura:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(rectangulo(base,altura))
        print(f"Agregando {figuras[n]} al contenedor...")

    elif n == 2:
        radio = float(input("Inserte el radio:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(circulo(radio))
        print(f"Agregando {figuras[n]} al contenedor...")
    
    elif n == 3:
        lado1 = float(input(f"Inserte el lado 1:\t"))
        lado2 = float(input(f"Inserte el lado 2:\t"))
        lado3 = float(input(f"Inserte el lado 3:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(triangulo(lado1,lado2,lado3))
        print(f"Agregando {figuras[n]} al contenedor...")
    
    elif n == 4:
        diag_min = float(input(f"Inserte la diagonal menor:\t"))
        diag_may = float(input(f"Inserte la diagonal mayor:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t\t{i}")
        instack_prcs[1].append(rombo(diag_min,diag_may))
        print(f"Agregando {figuras[n]} al contenedor...")

    elif n == 5:
        lados = int(input("Numero de lados del poligono:\t"))
        apotema = int(input("Inserte el apotema:\t"))
        lado = float(input("Inserte el lado:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(poligono(apotema,lados,lado))
        print(f"Agregando {figuras[n]} al contenedor...")


print("_".center(50,"_",),"\nMOSTRANDO CONTENEDOR\t(Queue Method)")
while True: # Ejecutando el metodo fifo
    print(f"\nOperaciones en el contenedor: ".ljust(50,"·"),"\n")
    
    # Listando operaciones dentro de la pila (FIFO)
    for w in range(len(instack_prcs[0])):
        print(f"{w+1}) Container ID: {instack_prcs[0][w]}")
    
    # Imprimiendo el ultimo dato en entrar
    print(f"\nEl ÁREA de {instack_prcs[0].pop(0)} es:\t{instack_prcs[1].pop()}")

    # Si no hay procesos pendientes romper el ciclo
    if instack_prcs[1] != []:
        print(f"\n· El contenedor aun tiene {len(instack_prcs[0])} elementos.")
    else:
        print(f"\n· El contenedor esta vacio.")
        break
