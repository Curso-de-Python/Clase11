'''
-----------------------------
 EJERCICIO N°3
 Ejemplos de excepciones
-----------------------------
'''
# INDEXERROR
# Otra manera de salir del bucle

lista = [1, 2, 3, 4, 5]
i = 0
flag = True

while flag:
  try:
    print(lista[i])
    i += 1
  except IndexError:  # cuando i=5
    flag = False

print('Listo')

'''
# ----------------------------
# KEYBOARD INTERRUPT
# Este programa no puede terminarse con Ctrl-C
from time import sleep
seconds = 0
while True:
  try:
    print(seconds)
    seconds += 1
    sleep(1)
  except KeyboardInterrupt:
    print("¡No hagas eso!")

# ----------------------------
# MEMORY ERROR
# Cuidado con este programa en el IDLE
string = 'x'
try:
  while True:
    string = string + string
    print(len(string))
except MemoryError:
  print('¡Esto no es gracioso!')

# ----------------------------
# OVERFLOW ERROR
# Valores e^k cuando k = 1, 2, 4, 8, 16, ...
from math import exp
e = 1
try:
  while True:
    print(exp(e))
    e *= 2
except OverflowError:
  print('El número es demasiado grande.')

# ----------------------------
# IMPORT ERROR
# una de estas importaciones fallará, ¿cuál será?
try:
  import math
  import time
  import abracadabra

except:
  print('Una de sus importaciones ha fallado.') # ¿cuál?

# ----------------------------
# KEY ERROR
# Cómo ganarle al diccionario

dict = {'a':'b', 'b':'c', 'c':'d'}
ch = 'a'
try:
  while True:
    ch = dict[ch]
    print(ch)
except KeyError:
  print('No existe tal clave:', ch)
'''
