name = 'Zed A. Shaw'
age = 35 # not a lie
inches_height = 74 # inches
cent_height = inches_height * 2.54
lbs_weight = 180 #lbs
kilo_weight = lbs_weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {inches_height} inches tall.")
print(f"He's {round(cent_height)} centimeters tall.")
print(f"He's {lbs_weight} pounds heavy.")
print(f"He's {round(kilo_weight)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes}eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + cent_height + kilo_weight
print(f"If i add {age}, {cent_height}, and {kilo_weight} I get {total}.")