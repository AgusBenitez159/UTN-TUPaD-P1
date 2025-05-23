# TP 4 - Estructuras repetitivas
# Tomás Agustín Benítez
# Ejercicios de práctica

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range (101):
    print(num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un numero: "))

if num == 0:
    dig = 1
else:
    dig = 0
while num > 0:
    num = num // 10
    dig +=1

print (f"Su numero tiene {dig} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

prim = int(input("Ingrese el primer valor: "))
seg = int(input("Ingrese el segundo valor: "))
sum = 0

for comp in range (prim + 1, seg):
    sum += comp
print(sum)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

num = int(input("Ingrese un numero: "))
sum = 0

while num != 0:
    sum += num
    num = int(input("Ingrese un numero: "))
print("La suma total es: ", sum)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num = random.randint(1, 9)

intento =  int(input("Pruebe adivinar el numero del 0 al 9: "))
cant_intentos = 1

while intento != num:
    intento = int(input("¡Numero equivocado, intente de nuevo!: "))
    cant_intentos += 1
print(f"¡Lo lograste en el intento N° {cant_intentos}!")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for num in range(100,-1,-1):
    if num % 2 == 0:
        print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.
sum = 0
num = int(input("Ingrese un numero: "))

for x in range (num+1):
    sum += x
print("La suma de los numeros es: ",sum)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el  programa 
# debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos 
# y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, 
# pero debe estar preparado para procesar 100 números con un solo cambio).

positivos = 0
negativos = 0
cont_impar = 0
cont_par = 0
ceros = 0
max = 100

for x in range (1, max+1):
    num = int(input(f"Ingrese el numero {x}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f"La cantidad de positivos es {positivos}, la cantidad de negativos es {negativos}")
print(f"La cantidad de pares es {cont_par}, la cantidad de impares es {cont_impar}")
print(f"La cantidad de ceros es {ceros}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor)

sum = 0
valor_max = 100

for x in range (1, valor_max+1):
    num = float(input(f"Ingrese el numero {x}: "))
    sum += num
media = sum / valor_max
print("La media es", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero: "))
invertido = ""

while num > 0:
    ultimo = num % 10
    invertido = invertido + str(ultimo) 
    num = num // 10

print("El numero invertido es", invertido)