# ERRORES
import math

x = float(input("Ingresa x: "))
y = math.sqrt(x)

print("La raíz cuadrada de", x, "es igual a", y)

# -----------------------------------
# MANEJO DE EXCEPCIONES

numero1 = int(input("Ingresa el 1er numero: "))
numero2 = int(input("Ingresa el 2do numero: "))

if numero2 != 0:
  print(numero1 / numero2)
else:
  print("Esta operacion no puede ser realizada.")

# try-except (muestra)
try: 
  print(numero1 / numero2)
except ZeroDivisionError:
  print("¿Intentaste dividir entre cero?")
