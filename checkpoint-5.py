# 1.  Cree un bucle For de Python
players = ('Remiro', 'Oriozola', 'Merino', 'Becker')

for player in players:
   print(player)


# 2.  Cree una función de Python llamada suma 
# que tome 3 argumentos y devuelva la suma de los 3.

def suma(Arg1, Arg2, Arg3):
   return {Arg1 + Arg2 + Arg3}


total = suma(54, 5, 21)
print(total)

# 3. •	Cree una función lambda con la misma funcionalidad 
# que la función de suma que acaba de crear.

suma2 = lambda Arg1, Arg2, Arg3: {Arg1 + Arg2 + Arg3}


print(suma2(54, 6, 21))

"""
4. Utilizando la siguiente lista y variable, determine si el valor 
de la variable coincide o no con un valor de la lista. *Sugerencia, 
si es necesario, utilice un bucle for in y el operador in.
"""
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

nombre = 'Enrique'

if nombre in lista_nombre:
  print(f'El usuario {nombre} está incluido en la lista')
else:
  print(f'Lo siento el usuario {nombre} no se encuentra en la lista')
