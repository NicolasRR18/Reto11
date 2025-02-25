# Reto11

=============================================================

El objetivo era resolver el reto 10, el cual consistia en
investigar metodos de strings, para saber su uso y cual es
su funcion, y tambien consistia en realizar el procesado 
del archivo adjunto y extraer ciertos items
A continuacion adjunto la imagen del repo del profe Felipe:

=============================================================

![image](https://github.com/user-attachments/assets/fed7f9aa-b320-4239-ace3-48a83abf5faf)

=============================================================

#Punto 1


-startswith() y endswith()

Indican si la cadena en cuestión comienza o termina 
con el conjunto de caracteres pasados como argumento, 
y retornan True o False en función de ello.

``` python

s = "Hola mundo"
print(s.startswith("Hola"))    # True
print(s.endswith("mundo"))     # True
print(s.endswith("world"))     # False

```

-isalpha()

Devuelve True si la cadena es todo carácteres alfabéticos

``` python

c = "ABC10034po"
c.isalpha()
#False

```
``` python

"Holamundo".isalpha()
#True

```

-isalnum()

Devuelve True si la cadena es todo números o carácteres 
alfabéticos

``` python

c = "ABC10034po"
c.isalnum()
#True

```

-isdigit()

Devuelve True si la cadena es todo números 
(False en caso contrario)

``` python

c = "100"
c.isdigit()
#True

```

-isspace()

Devuelve True si la cadena es todo espacios

``` python

"  -  ".isspace()
#False

```

-istitle()

Devuelve True si la primera letra de cada palabra 
es mayúscula

``` python

"Hola Mundo".istitle()
#True

```

-islower()

Devuelve True si la cadena es todo minúsculas

``` python

"Hola mundo".islower()
#False

```

-isupper()

Devuelve True si la cadena es todo mayúsculas

``` python

"Hola mundo".isupper()
#False

```

Tomado de:

-https://recursospython.com/guias-y-manuales/30-metodos-de-las-cadenas/

-https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-las-cadenas/

=============================================================

#Punto 2

Procesar el archivo y extraer:

Cantidad de vocales
Cantidad de consonantes
Listado de las 50 palabras que más se repiten

-el codigo para la solucion del ejercicio se encuentra adjuntada al repositorio
