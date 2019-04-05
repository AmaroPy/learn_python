from sys import argv

script, filename = argv

# with open es BIEN
with open(filename, 'r') as document:
    print("Here's your file".format(filename))
    print(document.read())
