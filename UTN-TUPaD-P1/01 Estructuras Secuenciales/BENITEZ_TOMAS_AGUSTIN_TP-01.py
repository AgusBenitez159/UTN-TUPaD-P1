# TP 1 - Tomás Agustín Benítez
# Ejercicios de práctica

# 1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por 85pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa "Marcos", el programa debe imprimir por pantalla "Hola Marcos!". Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa "Marcos", "Pérez", "30" y "Argentina", el programa debe imprimir "Soy Marcos Pérez, tengo 30 años y vivo en Argentina". Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print (f"{numero} multiplicado por 1 es {numero * 1}")
print (f"{numero} multiplicado por 2 es {numero * 2}")
print (f"{numero} multiplicado por 3 es {numero * 3}")
print (f"{numero} multiplicado por 4 es {numero * 4}")
print (f"{numero} multiplicado por 5 es {numero * 5}")
print (f"{numero} multiplicado por 6 es {numero * 6}")
print (f"{numero} multiplicado por 7 es {numero * 7}")
print (f"{numero} multiplicado por 8 es {numero * 8}")
print (f"{numero} multiplicado por 9 es {numero * 9}")
print (f"{numero} multiplicado por 10 es {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
#(Todavia no vimos condicionales ni bucles:p)
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
print (f" La suma de {num1} + {num2} es {num1+num2}")
print (f" La resta de {num1} - {num2} es {num1-num2}")
print (f" La multiplicación de {num1} * {num2} es {num1*num2}")
print (f" La división de {num1} / {num2} es {num1/num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índicede masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso / altura^2

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc :.1f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: F = C * 1.8 + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.1f} grados Fahrenheit.")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.1f}")
