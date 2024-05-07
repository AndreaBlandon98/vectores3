cantidad_productos = int(input("Ingrese la cantidad de productos: "))

productos = {}

for i in range(cantidad_productos):
    nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
    precio_producto = float(input(f"Ingrese el precio del producto {nombre_producto}: "))
    productos[nombre_producto] = precio_producto

costo_total = sum(productos.values())

print(f"El costo total a gastar en los productos es: {costo_total}")
