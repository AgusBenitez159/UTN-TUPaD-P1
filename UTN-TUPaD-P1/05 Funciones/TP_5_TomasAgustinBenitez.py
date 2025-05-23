# TP 5 - Funciones
# Tomás Agustín Benítez
# Ejercicios de práctica

#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo ():
    print("Hola mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de￾volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra￾dio como parámetro y devuelva el área del círculo. 
# calcular_peri￾metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.14 * (radio * radio)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es {area} y el perímetro es {perimetro}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta funcion.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

segundos = int(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos}s equivale a {horas} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")


numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    print(f"El resultado de la suma es {a+b}")
    print(f"El resultado de la resta es {a-b}")
    print(f"El resultado de la multiplicacion es {a*b}")
    print(f"El resultado de la division es {a/b}")

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
operaciones_basicas(a,b)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado 
# con dos decimales.

def calcular_imc(peso, altura):
    IMC = peso / altura ** 2
    return IMC

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
IMC = calcular_imc(peso, altura)
print(f"Su IMC es de {IMC:.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}° en fahrenheit seria {fahrenheit}°")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a+b+c) / 3
    return promedio

primero = float(input("Ingrese el primer numero: "))
segundo = float(input("Ingrese el segundo numero: "))
tercero = float(input("Ingrese el tercero numero: "))

promedio = calcular_promedio(primero, segundo, tercero)
print(f"El promedio de los tres números es: {promedio:.1f}")