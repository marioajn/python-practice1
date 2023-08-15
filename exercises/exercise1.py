"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5*5

# COMPLETAR - INICIO
area_cuadrado = lado_cuadrado
# COMPLETAR - FIN
print(lado_cuadrado)

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5**2

# COMPLETAR - INICIO
print(lado_cuadrado)
# COMPLETAR - FIN
area_cuadrado = lado_cuadrado
assert area_cuadrado == 25


"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = pow( 5, 2)
print(lado_cuadrado)
# COMPLETAR - INICIO

# COMPLETAR - FIN
area_cuadrado = lado_cuadrado
assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

cantidad_a_comprar =int(presupuesto_disponible/precio)
# COMPLETAR - INICIO
print(cantidad_a_comprar)
# COMPLETAR - FIN

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1
es_divisible_por_siete=numero_incalculable%7
# COMPLETAR - INICIO
print(es_divisible_por_siete)
# COMPLETAR - FIN

assert es_divisible_por_siete==0