name = str(input("What is your full name? "))
name.capitalize()
if name[-1] == " ":
    print("you have not entered a valid name please try again")
else:
    gap = (name.find(" "))
    first_name = name[:gap]
    last_name = name[gap+1:]

    first_split = int(len(first_name)/2)
    last_split = int(len(last_name)/2)

    f_half_1 = first_name[:first_split]
    f_half_2 = first_name[first_split:]
    s_half_1 = last_name[:last_split]
    s_half_2 = last_name[last_split:]

    name_mix_1 = (f_half_1 + s_half_1).capitalize() + " " + (f_half_2 + s_half_2).capitalize()
    name_mix_2 = (f_half_2 + s_half_2).capitalize() + " " + (f_half_1 + s_half_1).capitalize()

    print("Your new name is either", name_mix_1, "or", name_mix_2)
