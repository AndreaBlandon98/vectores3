numeros = []

n = int(input("Ingrese la cantidad de números: "))

for i in range(n):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es: {cuadrado}")

