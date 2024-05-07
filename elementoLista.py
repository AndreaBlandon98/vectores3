elementos = input("Ingrese los elementos de la lista separados por espacios: ").split()

elemento_a_buscar = input("Ingrese el elemento que desea buscar: ")

if elemento_a_buscar in elementos:
    posiciones = [i for i, x in enumerate(elementos) if x == elemento_a_buscar]
    if len(posiciones) > 1:
        print(f"El elemento {elemento_a_buscar} se encuentra en las posiciones: {posiciones}")
    else:
        print(f"El elemento {elemento_a_buscar} se encuentra en la posición: {posiciones[0]}")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")