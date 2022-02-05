#Escribir una función que aplique un descuento a un precio y otra que aplique
#el IVA a un precio. Escribir una tercera función que reciba un diccionario con
# los precios y porcentajes de una cesta de la compra, y una de las funciones
# anteriores, y utilice la función pasada para aplicar los descuentos o el IVA
# a los productos de la cesta y devolver el precio final de la cesta.

def descuento(precio, desc):
    pagar = precio - (precio*desc/100)
    return pagar
def iva(precio, iva=21):
    pagara = precio + (precio*iva/100)
    return pagara
def diccionario(diccionario_compras, funcion):
    total = 0
    for price, discount in compras.items():
        total += funcion(price, discount)
    return total

compras = {100:10, 200:10, 250:10}
print(f"El precio con descuento es: {diccionario((compras),descuento)}")
print(f"El precio con iva es: {diccionario((compras),iva)}")
