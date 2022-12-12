# Program:  Calculadora de Perimetro (Return ID from container)
# Method:   Stack (pilas)
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
    pmtro = 4 * l
    return pmtro

def rectangulo(b,h):
    pmtro = (b + h) * 2
    return pmtro

def circulo(r):
    pmtro = 2 * (pi * r)
    return pmtro

def triangulo(l1,l2,l3):
    pmtro = l1 + l2 + l3
    return pmtro

def rombo(dma,dmi):
    pmtro = (0.5 * ((dma**2) + (dmi**2))) * 2
    return pmtro

def poligono(ls,l):
    pmtro = ls * l
    return pmtro

# User view
print(f"Bienvenido a la calculadora de areas".center(75))
print(f" Kalkucan ".center(75,"="))

size = int(input("¿Cuantas operaciones desea agregar?\t")) # Definir la cantidad de operaciones para el ciclo
for i in range(size):
    print("\n>>> Estas son algunas figuras disponibles, seleccione el número correspondiente.")
    
    for j in range(len(figuras)): # Listado figuras disponibles
        print(f"{j+1}) {figuras[j]}")

    while True: # Ciclo permanente siempre y cuando no se seleccione una figura valida
        row += 1
        print(f"\n· Figura Geometrica {row}")
        n = int(input(f"Introduzca el número correspondiente y presione enter.\t"))-1
        if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
            print(f"Ha seleccionado con exito la figura {figuras[n]}")
            break
        else:
            print(f"Seleccione una figura valida")
            continue

    if n == 0: # 
        lado = float(input("Inserte el lado:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}") # Ingresa nombre e indice de figura
        instack_prcs[1].append(cuadrado(lado))      # Resultado de la función
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 1:
        base = float(input("Inserte el lado:\t"))
        altura = float(input("Inserte la altura:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(rectangulo(base,altura))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 2:
        radio = float(input("Inserte el radio:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(circulo(radio))
        print(f"Agregando {figuras[n]} al contenedor")
    
    elif n == 3:
        lado1 = float(input(f"Inserte el lado 1:\t"))
        lado2 = float(input(f"Inserte el lado 2:\t"))
        lado3 = float(input(f"Inserte el lado 3:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(triangulo(lado1,lado2,lado3))
        print(f"Agregando {figuras[n]} al contenedor")
    
    elif n == 4:
        diag_min = float(input(f"Inserte la diagonal menor:\t"))
        diag_may = float(input(f"Inserte la diagonal mayor:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t\t{i}")
        instack_prcs[1].append(rombo(diag_min,diag_may))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 5:
        lados = int(input("Numero de lados del poligono:\t"))
        lado = float(input("Inserte el lado:\t"))
        instack_prcs[0].append(f"{figuras[n]}\t{i}")
        instack_prcs[1].append(poligono(lados,lado))
        print(f"Agregando {figuras[n]} al contenedor")


print("_".center(50,"_",),"\nMOSTRANDO CONTENEDOR\t(Stack Method)")
while True: # Ejecutando el metodo lifo
    print(f"\nOperaciones en el contenedor: ".ljust(50,"·"),"\n")
    
    # Listando operaciones dentro de la pila (LIFO)
    for w in range(len(instack_prcs[0])):
        print(f"{w+1}) Container ID: {instack_prcs[0][w]}")
    
    # Imprimiendo el ultimo dato en entrar
    print(f"\nEl PERÍMETRO de {instack_prcs[0].pop()} es: {instack_prcs[1].pop()}")

    # Si no hay procesos pendientes romper el ciclo
    if instack_prcs[1] != []:
        print(f"\n· El contenedor aun tiene {len(instack_prcs[0])} elementos.")
    else:
        print(f"\n· El contenedor esta vacio.")
        break
