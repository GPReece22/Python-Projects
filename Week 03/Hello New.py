name = str(input("What's your name"))
new_name = name.capitalize()

# if the first thing is a space this breaks, fix the same way??
if new_name[:3] == "Sir":
    new_name = new_name[4:]
    new_name = new_name.capitalize()

if new_name == "Arthur":
    print("My Liege! It is good to meet you")

if new_name == "":
    print("Hello, World")

else:
    print("Hello Sir", new_name, "It's nice to meet you")
# must be a neater way to do this than 3 if statements
