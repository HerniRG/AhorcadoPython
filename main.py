import random
import os

from dibujo import dibujar_ahorcado
from palabras import palabras

def seleccionar_palabra(lista_palabras):
    # Selecciona una palabra al azar de la lista
    palabra = random.choice(lista_palabras)
    return palabra

def limpiar_pantalla():
    # Limpia la pantalla dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')



def jugar_ahorcado(palabra):
    # Inicializa la palabra oculta
    palabra_oculta = '_' * len(palabra)
    letras_adivinadas = []
    intentos = 6

    limpiar_pantalla()
    print("¡Bienvenido al juego de Ahorcado!\n")
    print("La palabra tiene {} letras.".format(len(palabra)))
    print("Adivina la palabra: ", palabra_oculta)

    while intentos > 0 and '_' in palabra_oculta:
        letra = input("Introduce una letra: ").lower()
        limpiar_pantalla()

        if letra in letras_adivinadas:
            print("Ya has intentado esta letra. Inténtalo de nuevo.")
            dibujar_ahorcado(intentos)
            print("Palabra: ", palabra_oculta)
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien hecho! La letra '{}' está en la palabra.".format(letra))
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
        else:
            print("La letra '{}' no está en la palabra. Te quedan {} intentos.".format(letra, intentos - 1))
            intentos -= 1
        
        dibujar_ahorcado(intentos)
        print("Palabra: ", palabra_oculta)

    if '_' not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra: {}".format(palabra))
    else:
        print("¡Oh no! Te has quedado sin intentos. La palabra era: {}".format(palabra))

def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    nueva_palabra_oculta = ''
    for i in range(len(palabra)):
        if palabra[i] == letra:
            nueva_palabra_oculta += letra
        else:
            nueva_palabra_oculta += palabra_oculta[i]
    return nueva_palabra_oculta

# Función principal
def main():
    palabra = seleccionar_palabra(palabras)
    jugar_ahorcado(palabra)

if __name__ == "__main__":
    main()
