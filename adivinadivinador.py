import random 

print("Hola! Bienvenido a \"AdivinAdivinador\"")
print("En este juego el objetivo es adivinar el numero que Python generó!")
print("El numero va a estar entre el 0 y un numero que eligas")

while True:
    maximo = input("Ingrese el numero: ")
    if int(maximo) < 0:
        print("El numero debe ser mas grande que 0")
    else: 
        break

numero = random.randint(0,int(maximo))

while True:
    adivinanza = int(input("¿Que numero piensas que es?: "))
    if int(adivinanza) > int(numero): 
        print("El numero es mas chico")
    elif int(adivinanza) < int(numero): 
        print("El numero es mas grande")
    elif int(adivinanza) == int(numero): 
        print("Felicitaciones! Lo encontraste!")
        break
    
 

