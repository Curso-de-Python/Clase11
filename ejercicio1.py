'''
-----------------------------
 EJERCICIO N°1
 try-except
-----------------------------
'''
# Podemos perder instrucciones
try:
  print("1")
  x = 1 / 0
  #print("2")
except ZeroDivisionError:
  print("Oh cielos, algo salio mal...")

print("2")

'''
# ¿Cómo saber qué causó la excepción?
try:
  x = int(input("Ingresa un numero: "))
  y = 1 / x
except:
  print("Oh cielos, algo salio mal...")

# SOLUCIÓN
try:
  x = int(input("Ingresa un numero: "))
  y = 1 / x
  print(y)
except ZeroDivisionError:
  print("No puedes dividir entre cero, lo siento.")
except ValueError:
  print("Debes ingresar un valor entero.")
except:
  print("Oh cielos, algo salio mal...")

# ----------------------------
# JERARQUÍA DE LAS EXCEPCIONES
try:
  y = 1 / 0
except ZeroDivisionError:
  print("Uuuppsss...")

print("FIN.")

# ----------------------------
# MANEJO DE EXCEPCIONES

# Dentro de la función
def mate(n):
  try:
    return 1 / n
  except ArithmeticError:
    print("¡Problema aritmético!")
  return None

mate(0)

# Fuera de la función
def mate(n):
  return 1 / n

try:
  mate(0)
except ArithmeticError:
  print("¡Se lanzó una excepción!")
'''
