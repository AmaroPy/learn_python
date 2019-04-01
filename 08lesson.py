# Definir una variable
formatter = "{} {} {} {}"

# Al dar un formato con ".format()" los 4 valores que introducimos en los parentesis de format toman las cuatro posiciones de "{}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
# Da igual que las posiciones sean en lineas distintas siempre y cuand entén bien identadas
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))