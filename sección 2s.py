# 1. Cree un programa que tome la base y la altura de un triángulo e imprima su área.

base = float (input('ingrese la base del triangulo :'))
altura = float (input('ingrese la altura del triangulo :'))

area = (base * altura)/2

print ('el area del triangulo es de :', area )


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 2. Cree un programa que tome el radio de un círculo e imprima su área y perímetro.

radio = float(input('ingrese el radio de un circulo :'))

A = 3.1416 * radio ** 2 


print ('el area del circulo es ---> ', A)


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 3. Cree un programa que tome el lado de un cubo e imprima su volumen.

volumen = float(input("ingrese el lado de un cubo :"))

V = volumen ** 3

print ('el volumen de un cubo es --->', V)


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 4. Cree un programa que tome el precio de un producto e imprima su precio final al consumidor con un IVA de 19%

producto = int (input("ingrese el precio de el producto: "))
iva = producto * 1.19
total = producto + iva
print("el total del producto es:  " + str (total))


print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 5. cree un programa que tome el valor de un producto e imprima su precio final si éste tiene siempre un descuento del 10%.

valor_producto = float(input("Ingresa el valor del producto: "))

descuento = valor_producto * 0.10

precio_con_descuento = valor_producto - descuento

print(f"El precio original del producto es: ${valor_producto}")
print(f"Descuento del 10%: ${descuento}")
print(f"Precio con descuento: ${precio_con_descuento}")

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 6. Cree un programa que lea una cantidad e imprima un porcentaje a calcular requerido sobre esa cantidad

def calcular_porcentaje(numero, porcentaje):
    porcentaje_decimal = porcentaje / 100
    resultado = numero * porcentaje_decimal
    return resultado

numero = float(input("Ingresa el número: "))

porcentaje_str = input("Ingresa el porcentaje que deseas calcular: ")

porcentaje_str = porcentaje_str.rstrip('%')
porcentaje = float(porcentaje_str)

resultado = calcular_porcentaje(numero, porcentaje)

print(f"{porcentaje}% de {numero} es igual a {resultado}") 