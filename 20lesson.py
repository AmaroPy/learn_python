from sys import argv

script, input_file = argv

def print_all(f): # Se define la función de 
    print(f.read()) # imprimir todo el archivo

def rewind(f): # Va al primer byte del archivo
    f.seek(0)

def print_a_line(line_count, f): # se define la función para
    print(line_count, f.readline()) # imprimir linea a linea

current_file = open(input_file) # Fija la variable a lo que se abra del archivo que le das en el argumento

print("First let's print the whole file:\n")

print_all(current_file) # imprime todo el archivo

print("now let's rewind, kind of like a tape.")

rewind(current_file) # vuelve al inicio del archivo después de leerlo.

print("Let's print three lines:")

current_line = 1 # como fijamos la variable en 1 es la linea 1
print_a_line(current_line, current_file)

current_line += 1 # al sumar 1 a la variable de la linea, pasamos a la linea 2
print_a_line(current_line, current_file)

current_line += 1 # al sumar 1 a la variable de la linea, que ya era 2 ahora es 3
print_a_line(current_line, current_file)