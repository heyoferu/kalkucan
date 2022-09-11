import math
figuras = ["Esfera","Cubo","Prisma (Rectangular)","Cono","Cilindro"]

# Pila
# Indice 0 para Identificadores e Indice 1 para el resultado del retorno
inqueue_prcs = [[],[]]

# Variables necesarias para el script
pi = math.pi

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

print(f"Bienvenido a la calculadora de volumenes".center(75))
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
        radio = float(input("Inserte el radio: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(esfera(radio))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 1:
        lado = float(input("Inserte el lado: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(cubo(lado))
        print(f"Agregando {figuras[n]} al contenedor")

    elif n == 2:
        lado1 = float(input("Inserte el lado 1: "))
        lado2 = float(input("Inserte el lado 2: "))
        altura = float(input("Inserte la altura: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(prism(lado1,lado2,altura))
        print(f"Agregando {figuras[n]} al contenedor")
    
    elif n == 3:
        radio = float(input(f"Inserte el radio: "))
        altura = float(input(f"Inserte la altura: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(cono(radio,altura))
        print(f"Agregando {figuras[n]} al contenedor")
    
    elif n == 4:
        radio = float(input(f"Inserte el radio: "))
        altura = float(input(f"Inserte la altura: "))
        inqueue_prcs[0].append(f"{figuras[n]} {i}")
        inqueue_prcs[1].append(cilindro(radio,altura))
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
