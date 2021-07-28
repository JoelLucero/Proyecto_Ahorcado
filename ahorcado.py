import random
import csv
import time
imagen = ['''
    
    |   |
        |
        |
        |
        |
        =''', '''
    
    |   |
    O   |
        |
        |
        |
        =''', '''
    
    |   |
    O   |
    |   |
        |
        |
        =''', '''
    
    |   |
    O   |
   /|   |
        |
        |
        =''', '''
    
    |   |
    O   |
   /|\  |
        |
        |
        =''', '''
   
    |   |
    O   |
   /|\  |
    |   |
        |
        =''', '''
    
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =''', '''
    
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =''', '''
''']


archivo=open("palabras.csv")
data=list(csv.DictReader(archivo))
archivo.close()

print("Bienvenido al juego de ahorcado")
time.sleep(4)
print("El objetivo del juego es adivinar la palabra secreta letra por letra")
print("tienes 7 vidas, pierdes una vida cada  vez que te equivocas si te quedas sin vidas pierdes")
time.sleep(6)
 
print("Desea jugar con palabras de:\n",
                                    "a) Nombres de paisess\n",
                                    "b) Palabras al azar\n",
                                    "c) Equipos de futbol\n"
                                    "d) Animales\n",
                                    "e) Ropa")
time.sleep(4)
 
cat_seleccionada = input("Ingrese A-B-C-D-E para selccionar el grupo de palabras: ")

cant_palabras = len(data)

while True:
    if cat_seleccionada.lower() == "a":
        print("excelente a seleccionado marcas de coches")
        indice_pregunta = random.randrange(0, cant_palabras)
        palabra_secreta = data[indice_pregunta] ['paises']
        break

    elif cat_seleccionada.lower() == "b":
        print("excelente a seleccionado nombres de paises")
        indice_pregunta = random.randrange(0, cant_palabras)
        palabra_secreta = data[indice_pregunta] ['azar']
        break

    elif cat_seleccionada.lower() == "c":
        print("excelente a seleccionado nombres de paises")
        indice_pregunta = random.randrange(0, cant_palabras)
        palabra_secreta = data[indice_pregunta] ['equipos']
        break

    elif cat_seleccionada.lower() == "d":
        print("excelente a seleccionado nombres de paises")
        indice_pregunta = random.randrange(0, cant_palabras)
        palabra_secreta = data[indice_pregunta] ['animales']
        break

    elif cat_seleccionada.lower() == "e":
        print("excelente a seleccionado nombres de paises")
        indice_pregunta = random.randrange(0, cant_palabras)
        palabra_secreta = data[indice_pregunta] ['ropa']
        break
 
    else:
        print("Por favor seleccione una categoria valida")
        cat_seleccionada = input("Ingrese C para marcas de coches y P para nombres de paises: ")
 


def tablero(palabra_oculta, intentos):
    print(imagen[intentos])
    print(' ')
    print(palabra_oculta)
    

def run():

    word = palabra_secreta
    palabra_oculta = ['--'] * len(word)
    intentos = 0

    while True:
        tablero(palabra_oculta, intentos)
        letra_actual = str(input('Escoge una letra: '))
        
        letra = []
        
        for i in range(len(word)):
                if word[i] == letra_actual:
                        letra.append(i)
                
        if len(letra) == 0 :
                intentos +=1
                if intentos == 7 :
                        tablero(palabra_oculta, intentos)
                        print (' ')
                        print ('Perdiste :( La palabra correcta era  {} ' .format(word))
                        break 
        else:
               for i in letra:
                        palabra_oculta[i] = letra_actual     
        
        letra = []
        
        try:
                palabra_oculta.index('--')
        except ValueError:
                
                print (' ')
                print (' Felicidades encontraste la palabra',word)      
                break
                
if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()