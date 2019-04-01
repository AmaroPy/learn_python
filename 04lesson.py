# Cuántos coches hay
cars = 100

# Cuánto espacio hay en los coches
space_in_a_car = 4.0 # Si cambias el numero decimal por un número no_decimal, sigue funcionando.

# Cuántos conductores hay
drivers = 30

# Cuántos pasajeros hay
passengers = 90

# Cuántos coches no tienen conductor
cars_not_driven = cars - drivers

# Cuántos coches SI tienen conductor
cars_driven = drivers

# Cuántos huecos tenemeos en total con los coches que SI tienen conductor
carpool_capacity = cars_driven * space_in_a_car

# Cuántos pasajeros podemos llevar en el día de hoy
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars aviable.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can trasport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")