# Program:  Calculadora de volumenes (Return ID from container)
# Method:   Queue (pilas)
# Date:     September 11th, 2022

import math
cuerposG = ["Esfera","Cubo","Prisma (Rectangular)","Cono","Cilindro"]

# Pila
# Indice 0 para Identificadores e Indice 1 para el resultado del retorno
instack_prcs = [[],[]]

# Variables necesarias para el script
pi = math.pi    # Valor de Pi
row = 0
# Funciones para las figuras
def esfera(r):
    vol = (4/3 * pi)*(r**3)
    return vol

def cubo(l):
    vol = l**3
    return vol

def prism(l1,l2,h):
    ab = l1 * l2
    vol = ab * h
    return vol

def cono(r,h):
    ab = pi * r**2
    vol = (ab * h)/3
    return vol

def cilindro(r,h):
    ab = pi * r**2
    vol = ab * h
    return vol

# User view
print(f"Bienvenido a la calculadora de volumenes".center(75))
print(f" Kalkucan ".center(75,"="))

size = int(input("¿Cuantas operaciones desea agregar?\t")) # Definir la cantidad de operaciones para el ciclo
for i in range(size):
    print("\n<<< Estas son algunas figuras disponibles, seleccione el número correspondiente.")
    
    for j in range(len(cuerposG)): # Listado figuras disponibles
        print(f"{j+1}) {cuerposG[j]}")

    while True: # Ciclo permanente siempre y cuando no se seleccione una figura valida
        row += 1
        print(f"\n· Cuerpo Geometrico {row}")
        n = int(input(f"Introduzca el número correspondiente y presione enter.\t"))-1
        if n == 0 or n == 1 or n == 2 or n == 3 or n == 4:
            print(f"\nHa seleccionado con exito la figura {cuerposG[n]}")
            break
        else:
            print(f"Seleccione una figura valida")
            continue

    # Ingresa elementos (indice y resultados) a "stack_prcs"
    if n == 0: 
        radio = float(input("Inserte el radio:\t"))
        instack_prcs[0].append(f"{cuerposG[n]}\t{i}")  # Index
        instack_prcs[1].append(esfera(radio))         # Resultado volumen usando funciones
        print(f"Agregando {cuerposG[n]} al contenedor")

    elif n == 1:
        lado = float(input("Inserte el lado:\t"))
        instack_prcs[0].append(f"{cuerposG[n]}\t{i}")
        instack_prcs[1].append(cubo(lado))
        print(f"Agregando {cuerposG[n]} al contenedor")

    elif n == 2:
        lado1 = float(input("Inserte el lado 1:\t"))
        lado2 = float(input("Inserte el lado 2:\t"))
        altura = float(input("Inserte la altura:\t"))
        instack_prcs[0].append(f"{cuerposG[n]}\t{i}")
        instack_prcs[1].append(prism(lado1,lado2,altura))
        print(f"Agregando {cuerposG[n]} al contenedor...")
    
    elif n == 3:
        radio = float(input(f"Inserte el radio:\t"))
        altura = float(input(f"Inserte la altura:\t"))
        instack_prcs[0].append(f"{cuerposG[n]}\t{i}")
        instack_prcs[1].append(cono(radio,altura))
        print(f"Agregando {cuerposG[n]} al contenedor...")
    
    elif n == 4:
        radio = float(input(f"Inserte el radio:\t"))
        altura = float(input(f"Inserte la altura:\t"))
        instack_prcs[0].append(f"{cuerposG[n]} {i}")
        instack_prcs[1].append(cilindro(radio,altura))
        print(f"Agregando {cuerposG[n]} al contenedor...")


print("_".center(50,"_",),"\nMOSTRANDO CONTENEDOR\t(Queue Method)")
while True: # Ejecutando el metodo fifo
    print(f"\nOperaciones en el contenedor: ".ljust(50,"·"),"\n")
    
    # Listando operaciones dentro de la pila (FIFO)
    for w in range(len(instack_prcs[0])):
        print(f"{w+1}) Container ID:\t{instack_prcs[0][w]}")
    
    # Imprimiendo el ultimo dato en entrar
    print(f"\nEl VOLUMEN de {instack_prcs[0].pop(0)} es: {instack_prcs[1].pop()}")

   # Si no hay procesos pendientes romper el ciclo
    if instack_prcs[1] != []:
        print(f"\n· El contenedor aun tiene {len(instack_prcs[0])} elementos.")
    else:
        print(f"\n· El contenedor esta vacio.")
        break

