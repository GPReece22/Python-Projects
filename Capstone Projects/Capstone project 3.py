print("You are stranded in an abandoned facility")
print("Try to find your wat out")
print("available commands are written in CAPITAL letters")
print("Any other commands will end the program")
print("First try LOOK around the room for clues")
action_1 = str(input("What would you like to do: "))

if action_1.upper() == "LOOK":
    print("You see two doors one to your LEFT and one to your RIGHT")
    action_2 = str(input("What would you like to do: "))

    if action_2.upper() == "LEFT":
        print("You burst out into the courtyard")
        print("There is a GATE to your left that appears to lead to the outside")
        print("There are chain CUTTERS on the floor of the courtyard, as well as a pair of TIGHTS")
        action_3 = str(input("What would you like to do: "))

        if action_3.upper() == "GATE":
            print("The gate has a lock on it with a SYMBOL that looks like it could match up to a KEY")
            action_4 = str(input("What would you like to do: "))

            if action_4.upper() == "KEY":
                print("You see a KEY hung up on the other side of the courtyard")
                print("As you look back down a man starts sprinting towards you with HANDCUFFS in his hand ")
                action_5 = str(input("What would you like to do: "))

                if action_5.upper() == "HANDCUFFS":
                    print("You dodge his charge grabbing his handcuffs on the way")
                    print("As the man turns around you see a slight opening for the KEY")
                    print("He looks a little disoriented but larger than you there's no way you can take him down")
                    print("Unless... you stole have his HANDCUFFS")
                    action_6 = str(input("What would you like to do: "))

                    if action_6.upper() == "KEY":
                        print("You sprint to the key before the security guard can regain his balance")
                        print("The key works!")
                        print("As you frolic around the fields you feel faint and pass out in the flowers")
                        print("You wake up feeling a sudden sense of fulfillment in your life")
                        print("That was the most productive day you've had since starting uni")

                    elif action_6.upper() == "HANDCUFFS":
                        print("As you go to slam the handcuffs on the security guy he wrestles you to the ground")
                        print("You wake up feeling like you've been at camel for the last 72 hours")
                        print("You decide today isn't the day for uni")

                elif action_5.upper() == "KEY":
                    print("As you go to key the security guy wrestles you to the ground")
                    print("You wake up feeling like you've just had a month long trip to the John Smiths brewery")
                    print("You decide today isn't the day for uni")

            elif action_4.upper() == "SYMBOL":
                print("As you spend your time staring at the symbol you hear footsteps behind you")
                print("Suddenly a security guy wrestles you to the ground, and you pass out")
                print("You wake up feeling like you've made use of the echo falls 3 for £12 deal")
                print("You decide today isn't the day for uni")

        elif action_3.upper() == "CUTTERS":
            print("As you approach the cutters a security guard bursts in to the courtyard and the world goes black")
            print("You wake up from your 'dream' in your own bed ready to go on with your life")

        elif action_3.upper() == "TIGHTS":
            print("You pick up the tights, wondering why you just decided to do that")
            print("a sudden urge comes over you to put the tights on your HEAD")
            action_tights = str(input("What would you like to do: "))

            if action_tights.upper() == "HEAD":
                print("You wake up from your dream to find a pair of tights on your head")
                print("You have no idea how they got they, but you don;t mind")
                print("You decide to wear tights on your head to work the next day and regret every moment of it...")

            else:
                print("Of course you didn't, who puts tights on their head!")
                print("You wake up the next day and go back to your life as normal")

    elif action_2.upper() == "RIGHT":
        print("As you approach the door a burly looking security guard bursts through it and the world goes black")
        print("You wake up from your 'dream' in your own bed ready to go on with your life")


else:
    print("You can only do action in capital letters.")
