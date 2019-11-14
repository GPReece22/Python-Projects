import random
import string
pass_wrong = 0
options = string.ascii_letters + string.digits + string.punctuation
gen_length = 0
target_len = (random.randint(6, 12))
random_pass = ""
not_allowed = ("huddersfield", "justinbieber", "cheese", "canalside",)
generate = input("Would you like a random password generating? ")

if generate.lower() == "yes":
    while gen_length < target_len:
        random_pass += (random.choice(options))
        gen_length += 1
    print("Your random password is", random_pass)

else:
    username = input("Please enter username: ")
    not_allowed += (username,)
    stud_id = input("Please enter your student id: ")
    not_allowed += (stud_id,)

    while pass_wrong == 0:
        pass_1 = str(input("Please enter password: "))
        pass_2 = str(input("Please re-enter password: "))
        length = len(pass_1)

        if pass_1 == pass_2:
            if pass_1 in not_allowed:
                print("Not secure enough")
            if 6 < length < 12:
                print("Password changed")
                pass_wrong = 1
            else:
                print("Password must be between 6 and 12 characters")
        else:
            print("Passwords do not match")
