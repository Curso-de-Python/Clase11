'''
-----------------------------
 EJERCICIO N°2
 Instrucciones raise y assert
-----------------------------
'''
# LA INSTRUCCIÓN RAISE
# 1era aplicación
def mate(n):
  raise ZeroDivisionError

try:
  mate(0)
except ArithmeticError:
  print("¿Que pasó? ¿Un error?")

'''
# 2da aplicación
def mate(n):
  try:
    return n / 0
  except:
    print("¡Lo hice otra vez!")
    raise

try:
  mate(0)
except ArithmeticError:
  print("¡Ya veo!")

# ----------------------------
# ASSERT
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0
x = math.sqrt(x)

print(x)
'''
