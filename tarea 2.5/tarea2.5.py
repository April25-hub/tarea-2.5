
#Arzaba Diaz April
import random

# esta linea generara un numero aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# esta linea iniciara variable para el intento del usuario
intento = None

print("Adivina el numero entre 1 y 10")

# esta linea repetira  para que el usuario siga intentando
while intento != numero_secreto:
    # esta linea pedira al usuario que ingrese un numero
    intento = int(input("Introduce tu adivinanza: "))
    #esta linea comparara la adivinanza con el numero secreto
    if intento < numero_secreto:
        print("demasiado bajo intenta de nuevo")
    elif intento > numero_secreto:
        print("demasiado alto Intenta de nuevo")

print("felicidades Adivinaste el numero")
