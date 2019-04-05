from sys import argv

script, user_name, second_name = argv
prompt = 'Escribe tu respuesta aquí' #study drills

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")

print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do yo live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("How old are you %s?" % second_name)
age = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer. Nice.
And you are %r years old.
""" % (likes, lives, computer, age)) #study drills