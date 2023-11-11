# number = 5

# print('El valor de la variable es:', number)

# base = int(input('ingrese la base'))
# altura = int(input('ingrese altura'))

# resultado = base * altura

# print('el area del cuadrado es:' , resultado)

#-------------------------------------------------

#ejercicio numero (2)

# edad = int(input('ingrese su edad'))

# if edad < 18:
#     print ('eres menor de edad')
# elif edad  >= 18 and  edad <= 65: 
#     print('eres un adulto')
# else :
#     print('eres un adulto mayor')

# #-----------------------------------


# #ejercicio numero(3)

# edad = int(input('ingrese edad'))
# precio = float(input('ingrese el prtecio del producto'))

# if edad < 18 :
#     print('valor del producto' + str( precio * .90) )
# elif edad >= 65 : 
#     print('valor del producto' + str(precio * .85))
# else :
#     print('el costo de su producto es' + str(precio))    

# #----------------------------------------


# #ejercicio numero(4)

# puntuacion = int(input('ingrese puntuacion'))

# if puntuacion >=90 :
#     print('sobresaliente')
# elif puntuacion >= 80 and puntuacion <= 89 :
#     print('bueno')
# elif puntuacion >=70 and puntuacion <=79 :
#     print('satisfecho')
# elif puntuacion >= 60 and puntuacion <=69 :
#     print('necesita mejorar')
# else :
#     print('reprobado')

# #-------------------------------


# #ejercicio numero (5)
    
    
# salario = float(input('ingrese su salario anual'))

# if salario <= 10000 :
#     print('no se aplica impuesto')
# elif  salario > 10000  and salario <= 50000 :
#     print('debe pagar 10 % de impuesto ' + str(salario * .1))
# elif salario > 50000  and  salario <= 100000 :
#     print('debe pagar 20 % de impuesto' + str(salario * .2))    
# else :
#     print('debe pagar 30% de impuesto' + str(salario * .3))    
    
    
#-------------------------




#ejercicio numero (1)

# acendente= 0
# decendente = 11

# while acendente < 10:
#     acendente += 1
#     decendente -= 1
#     print(acendente, '/' , decendente)
    
    
#ejercicio numero (2)

# import random

# aleatoreo = random.randint (1, 100)
# adivina = 0

# while adivina != aleatoreo:
#     if adivina == 0:
#         print('inicia el juego')
#     elif adivina < aleatoreo:
#         print('demasiado bajo')    
#     else:
#         print('demasiado alto')    
#     adivina = int (input('ingresa el numero')) 
# print('has ganado')   

# bucles

# ejercicio 1 ------------------------


# numero = int(input("Ingrese un número:"))
# print(f"Tabla de multiplicar de {numero}:")
# for i in range(1, 11):
#     resultado = numero * i
    
#     print(f"{numero} x {i} = {resultado} " )

# ejercicio 2 ----------------

# numero = int(input("Ingrese un número entero: "))

# suma_enteros = 0

# for x in range(2, numero + 1, 2):
#     suma_enteros += x
    

# print(f"La suma de los números pares desde 2 hasta {numero} es: {suma_enteros}")

# Ejercicio 3 -----------------------

# lineas = 5

# for x in range (lineas + 1):
#     print('*' * x)
#  --------------------------


# -----------------------------

#condicionales y bucles

#ejercicio 1---------------------


# num = int(input("ingrese numero"))
# suma_pares = 0
# for x in range(1, num + 1):
#     if x % 2 == 0: 
#         suma_pares += x
#         print(f" suma de numeros pares desde 1 hasta {num} es: {suma_pares}")


#ejercicio 2 ----------------------

# palabra = input("Ingrese una palabra: ")

# contador_vocales = 0

# palabra = palabra.lower()

# indice = 0

# while indice < len(palabra):
#     caracter = palabra[indice]
#     if caracter in "aeiou":
#         contador_vocales += 1
#     indice += 1

# print(f"La cantidad de vocales en la palabra es: {contador_vocales}")


# Ejercicio 3 -------------------

# numero = int(input("Ingrese un número entero positivo mayor que 1: "))

# es_primo = True

# for i in range(2, int(numero**0.5) + 1):
#     if numero % i == 0:
#         es_primo = False
#         break


# if es_primo:
#     print(f"{numero} es un número primo.")
# else:
#     print(f"{numero} no es un número primo.")

# Ejercicio 4 -----------------------------------

# import random

# numero_secreto = random.randint(1, 100)

# print("¡Bienvenido al juego de adivinanzas!")
# print("Intenta adivinar el número secreto entre 1 y 100.")

# intentos = 0

# while True:
#     intento = int(input("Ingresa tu intento: "))
    
#     intentos += 1

#     if intento == numero_secreto:
#         print(f"¡Felicidades! ¡Adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
#         break
#     elif intento < numero_secreto:
#         print("Demasiado bajo. Intenta de nuevo.")
#     else:
#         print("Demasiado alto. Intenta de nuevo.")

# Ejercicio 5 -------------------------------

# numero = int(input("Ingrese un número: "))


# if numero % 2 == 0:
#     for i in range(numero):
#         print('*', end=' ')
# else:
#     for i in range(numero):
#         print('* ' * numero)