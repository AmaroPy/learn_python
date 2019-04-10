people = 50 #studi drills
cars = 30
buses = 45
# Python va comprobado linea a linea 
# Y si se cumple una de las lineas se salta el resto.
# En este caso comprueba la linea 12
# Si se cumple, continua en la linea 13
# Si no se cumple la linea 12 saltaría a la 15
# Y volvería a chequear. Así sucesivamente.
# Si ninguna condición se cumple, y tenemos un "else".
# El "else" se cumpliría siempre porque es la última opción
if cars > people: # planteamos la condición de mayor, menor o cualquier otro caso.
    print("We should take the cars.")

elif cars < people: 
    print("We should not take the cars.")

else:
    print("We can't decide")

if buses > cars: # otra condición pero en este caso entre autobuses y coches
    print("That's too many buses.")

elif buses < cars:
    print("Maybe we could take the buses.")

else:
    print("still can't decide.")

if people > buses: # otra condición pero entre personas y autobuses
    print("Alright, let's just take the buses.")

else:
    print("Fine, let's stay home then.")