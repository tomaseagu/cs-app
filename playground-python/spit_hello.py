# https://www.charset.org/utf-8

with open('hello.c', 'rb') as f:
    contenido = f.read()
    
    binario_completo = " ".join(f"{b:08b}" for b in contenido)

    print(binario_completo)
    
    print(list(contenido))



# El primer caracter # en binario es
# 0 0 1 0 0 0 1 1 <- binario que representa el #
# 7 6 5 4 3 2 1 0 <- elevamos a la 2 la posicion
# 128, 64, 32, 16, 8, 4, 2, 1
#  35 <- sumamoos solo los valores 1
# 35 es el decimal que representa el #

# Otra forma de representar el binario de # es con Hexadecimal
# El Hexadecimal es un sistema de 16 dígitos distintos para contar ( se invento para facilitar la lectura)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F <- El hex cuenta del 0 al 5
# (0 0 1 0) (0 0 1 1) <- se divide el binario en dos grupos
# (0 0 1 0) <- posiciones 3, 2, 1, 0 = 1^2 = 2
# (0 0 1 1) <- posiciones 3, 2, 1, 0 = (2^1) + (2^0) = 3 # cualquier num elevado a la 0 da 1
# esto nos da un valor de Hex 23 
#  Siendo su CodePoint de Unicode U+0023


# el valor de z en binario es (0101) (1010)
# Realizando las multiplicaiones debidas nos da 5,y 10
# En el sistema hex se representa con 5A
# siendo su Point Code U+005A

# U+ Sinifica que que viene a continuación es un número del catálogo de Unicode
# 005A número hexadecimal rellenado con ceros a la izquierda para que siempre tenga como mínimo, 4 dígitos
# Esta regla solo funciona para los primeros 128 caracteres (del 0 al 127) por que entran en un solo byte 
# utf 8 los deja intanctos para tener retrocompatbilidad con ASCII que funcionaba con 7 bits y puede representar 128 numeros diferentes
# el primer numero en UTF-8 funciona como un semaforo (si el binario comienza con 0 es ASCII y con 1 es UTF-8)
# Con 8 bits podemos representar hasta 255 numeros enteros pero utf 8 se detiene en el 127, y a  partir
# de ahi con el primer numero semaforo comienza a utilizar grupos de bytes


# Ejemplo de representacion del 128 
# Point Code U+0080	
# UTF-8 hex C2 80	
# Caracter: €	Euro Sign 



