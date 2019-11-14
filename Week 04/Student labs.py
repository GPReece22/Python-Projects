try:
    number_of_pupils = int(input("Enter number of pupils: "))

    while 1:
        if number_of_pupils > 0:
            number_of_pcs = int(input("Enter number of PC's per lab: "))
            break
        else:
            print("You have entered an incorrect number of pupils, please try again")
            number_of_pupils = int(input("Enter number of pupils: "))

    while 1:
        if number_of_pcs > 0:
            rooms_needed = (number_of_pupils // number_of_pcs) + 1
            print("You will need", rooms_needed, " lab(s) for that many pupils")
            break
        else:
            print("You have entered an incorrect number of pcs, please try again")
            number_of_pcs = int(input("Enter number of PC's per lab: "))

except ValueError:
    print("You have not entered a number")
