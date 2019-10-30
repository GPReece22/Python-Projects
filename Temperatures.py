choice = int(input("Would you like to convert 1.Celsius or 2. Fahrenheit"))
if choice == 1:
    temp_cel = float(input("Please enter a temperature in celsius "))
    temp_far = temp_cel * (9 / 5) + 32
    print("In fahrenheit that is ", temp_far)
else:
    temp_far = float(input("Please enter a temperature in fahrenheit "))
    temp_cel = ((temp_far-32) * (5/ 9))
    print("In celsius that is ", temp_cel)