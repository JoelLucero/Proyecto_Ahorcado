![logo](/imagenes/Python-Project-Ideas-big.jpg)


### :eyes: :eyes: PROYECTO AHORCADO :eyes: :eyes:

El juego del ahorcado es un juego clásico en el cual adivinas una palabra
El funcionamiento general del juego es el siguiente:

1.Se selecciona el tema sobre el cual se elegirá una palabra secreta

2.El juego elige la palabra secreta

3.Se le solicita al jugador adivinar la palabra secreta letra por letra

4.Si el jugador adivina sin equivocarse 7 veces gana en el caso opuesto pierde.

#### Descripcion
Para esta ocasión, se uso la programación en Python para mostrar, por consola este famoso y entretenido juego. De esta manera, todos recordaremos este juego que todos jugamos en nuestra niñez.
Ahora te muestro como realizar, paso a paso el juego del ahorcado en Python 3.7.7

#### Primera parte del juego

Esta primera parte del juego, es muy sencilla y básica. Aquí  importamos el módulo “random”; este modulo, nos será muy útil, para poder generar un dato aleatorio, para así elegir una palabra entre muchas. Estas palabras estarán contenidas en una lista que programaremos mas adelante.Tambien se importo csv donde se encuentra archivado todas las palabras y time libreria relacionada con el tiempi. 

Para hacer el juego mas interesante y parecido al original, se mostrara un dibujo con el que le haremos saber al jugador si está siendo ahorcado o no.

Este recurso será usado mas adelante, cuando el jugador se equivoque al ofrecer una letra.

#### Primer paso

Aquí realizamos el pequeño dibujo. Para así mostrarle al jugador, si está ahorcado o no.

![imagen](/imagenes/imagen.jpg)

#### Segundo paso

Al iniciar una partida en nuestro juego, estas serán las palabras importadas de un archivo csv con las que nuestro programa nos pondrá a prueba.

El programa nos preguntara con que grupo de palabras queremos jugar .

![palabras](/imagenes/elejir%20grupo%20paalabras.jpg)

#### Tercer paso
En este paso, definiremos algunas funciones, que nos permitirán mostrar mensajes en la consola con la letra elejida . Además se nos mostrara un dibujo “distinto”. Ya que se irá completando, hasta estar totalmente ahorcado.


Esto podemos hacerlos mediante los comandos if, elif y else
 
![palabras](/imagenes/programa.jpg)
