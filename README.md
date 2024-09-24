# tarea-2.5
arzaba_ diaz _april
#esta linea dira mi nombre
#Arzab Diaz April

#esta linea dira el numero de programa

#tarea 2.5

import random

#esta linea almacenara un numero aleatorio entre 1 y 1000

numero_secreto = random.randint(1, 1000)

print("bienvenido al juego de adivinar el numero")

print("haz elegido un número entre 1 y 100 ¿Puedes adivinar cual es?")

#esta linea iniciara el contador de intentos


intentos = 0

while True:

    #esta linea pedira al usuario que adivine el numero
    
    try:
    
        adivinanza = int(input("ingresa tu adivinanza:"))
        intentos += 1

        
        
        if adivinanza < numero_secreto:
        
            
            print("demasiado bajo  Intenta de nuevo")
        elif
        adivinanza > numero_secreto:
        
            print("demasiado alto Intenta de nuevo")
        else
        :
        
            print("Felicidades adivinaste el numero {numero_secreto} en {intentos} intento")
            
            break
    except v
    alueerror:
    
        print("por favor, ingresa un numero valido")
        ![image](https://github.com/user-attachments/assets/a745c0e5-d0a7-4a4e-bc8d-a9ee9cb1e6fb)
        ![image](https://github.com/user-attachments/assets/b148d9c4-8f88-43e4-b01f-f9f840f874cc)






