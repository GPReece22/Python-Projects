try:
    number_of_pupils = int(input("Enter number of pupils"))
    number_of_sweets = int(input("Enter number of sweets"))

    sweets_each = number_of_sweets // number_of_pupils
    left = number_of_sweets % number_of_pupils

    print("Each pupil will get ", sweets_each, "sweets each")
    print("There will be ", left, "sweets left")

except ZeroDivisionError:
    print("Invalid details entered ")
