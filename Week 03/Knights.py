knights = ("robin", "galahad", "bors", "bedevere")
print("All the knights are", knights)
print(type(knights))

# first entry
print("The first knight is", knights[0])
# last entry
print("The last knight is", knights[-1])
# third entry
print("The third knight is", knights[2])

knights += ("Launcelot",)
print("Launcelot has entered the arena")
print("All of the knights are", knights)
