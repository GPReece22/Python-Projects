import string
import random
letters = string.ascii_lowercase
tiles = ""
words = """art
hue
ink
oil
pen
wax
clay
draw
film
"""

for i in range(8):
    tiles += random.choice(letters)
valid_words = ()
start = 0
end = 0
found_words = ()
print(tiles)

for char in words:
    if char == "\n":
        valid_words = valid_words + (words[start:end],)
        start = end + 1
        end = end + 1
    else:
        end = end + 1

for word in valid_words:
    tiles_left = tiles
    for letter in word:
        if letter not in tiles_left:
            break
        else:
            index = tiles_left.find(letter)
            tiles_left = tiles_left[:index]+tiles_left[index+1:]
        if len(word) == len(tiles)-len(tiles_left):
            found_words = found_words + (word,)
print(valid_words)
print(found_words)





