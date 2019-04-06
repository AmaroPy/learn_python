def cheese_and_crackers(cheese_count, boxes_of_crackers): # Aquí define la función nombre y (parametro1, parametro 2)
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers" % boxes_of_crackers)
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # Se dan los parámetros directamente

print("OR, we can use variables from our script:")
amount_of_cheese = 10 # Se dan los parámetros a través de variables
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
cheese_and_crackers(10 + 20, 5 + 6) # Se dan los parámetros usando matemáticas

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# Se dan los parámetros usando variables 
# y usando matemáticas sobre dichas variables

def gatos_y_perros(gatos, perros): #Aquí se define la función.
    print("Tienes %d gatos" % gatos)
    print("Tienes {} perros\n".format(perros))

print("Dando los parámetros directamente")
gatos_y_perros(2, 3)

print("Dando los parámetros a través de variables")
valor_gatos = 2
valor_perros = 3

gatos_y_perros(valor_gatos, valor_perros)