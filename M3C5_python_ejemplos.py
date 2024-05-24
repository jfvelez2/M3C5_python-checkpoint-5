# Condicionales:

# 1. Condicional 'if' 
tiempo_Donostia = 'soleado'

if tiempo_Donostia == 'soleado':
  print('Voy a la playa!') # Resultado --> Voy a la playa!


# 2. Condicional 'if-else"
tiempo_Donostia = 'nublado'

if tiempo_Donostia == 'soleado':
  print('Voy a la playa!') 
else:
  print('Me quedaré en casa descansando') # Resultado --> Me quedaré en casa descansando


# 3. Condicional 'if-elif-else'
temperatura_Donostia = 30

if temperatura_Donostia < 15:
  print(f'Hace frío para ir a la playa')
elif temperatura_Donostia > 40:
  print(f'Hace demasiado calor para ir a la playa')
else:
  print(f'{temperatura_Donostia}ºC es una temperatura adecuada para ir a la playa')
  # Resultado --> 30ºC es una temperatura adecuada para ir a la playa

# Por ejemplo en una colección de caracteres
alfabeto = 'abcdef'

for letras in alfabeto:
  print(letras)
# Resultado:
# a
# b
# c
# d
# e
# f

# Ejemplo con una lista tipo diccionario, par clave:valor:
jugadores = {
  'Guardameta': 'Remiro',
  'Defensa': 'Oriozola',
  'Centrocampista': 'Merino',
  'Atacante': 'Becker'
}

# Iterará sobre el par clave-valor en la colección del diccionario:
for posicion, jugador in jugadores.items():
  print('Nombre del jugador:', jugador)
  print('Posición', posicion)
  # Resultado:
# Nombre del jugador: Remiro
# Posición Guardameta
# Nombre del jugador: Oriozola
# Posición Defensa
# Nombre del jugador: Merino
# Posición Centrocampista
# Nombre del jugador: Becker
# Posición Atacante

# Ejemplo con bucle while
flores = 1
while flores <= 10:
    print('Riega la flor # ' + str(flores))
    flores += 1

"""
#Resultado:
Riega la flor # 1
Riega la flor # 2
Riega la flor # 3
Riega la flor # 4
Riega la flor # 5
Riega la flor # 6
Riega la flor # 7
Riega la flor # 8
Riega la flor # 9
Riega la flor # 10
"""

# Ejemplo de lista por comprensión
numeros = [1, 2, 3, 4]

# uso de listas por comprensión para crear una nueva lista
duplicar_numeros = [num * 2 for num in numeros]

print(duplicar_numeros)
# Resultado:
# [2, 4, 6, 8]

# Definimos una variable donde se almacenarán los elementos de la lista
num_list = range(1, 11)

# 1. Forma tradicional
even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

print(even_numbers) # --> [2, 4, 6, 8, 10]

# 2. Utilizando lista por comprensión
even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list)) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers) # --> [2, 4, 6, 8, 10]