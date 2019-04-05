from sys import argv
script, first, second, third, fourd = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Yout fourd variavle is:", fourd)

# ejecutar:
# python 13Joseslesson.py hola mundo hey
# python 13Joseslesson.py esto escribe aquí

# respecto a los argv, has definido todo en una linea, porque es un array
mi_array = [1,2,3,4]

uno, dos, tres, cuatro = mi_array

# tambien

otro_uno = mi_array[0]
otro_dos = mi_array[1]
otro_tres = mi_array[2]
otro_cuatro = mi_array[3]

print("Tu primer variable es:", otro_uno)
print("Tu segunda variable es:", input("escribe tu nombre aquí> "))
print("Tu tercera variable es:", otro_tres)
print("Tu cuarta variable es:", otro_cuatro)
