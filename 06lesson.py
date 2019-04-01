# Define la variable de types_of_people y la incluye en una variable tipo string
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Define dos variables y las incluye en otra tercera variable 
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}.."

# Imprime las dos variables anteriores
print(x)
print(y)

# Vuelve a imprimir las dos mismas variables pero incluyendolas a otro string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Define otras dos variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Imprime dichas variables cambiendo el formato para que puedan ser impresas como string
print(joke_evaluation.format(hilarious))

# Define dos variables tipo string
w = "This is the left side of..."
e = "a string with a right side."

# Imprime las dos variables con el + para concatenarlas
print(w + e)