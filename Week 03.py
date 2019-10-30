name = input("Enter the students name: ")

mark_1 = int(input("Enter the first result: "))
mark_2 = int(input("Enter the second result: "))
mark_3 = int(input("Enter the third result: "))
mark_4 = int(input("Enter the fourth result: "))
mark_5 = int(input("Enter the fifth result: "))

total = mark_1 + mark_2 + mark_3 + mark_4 + mark_5
avg = total / 5

print("The average mark for", name, "is", (str(avg)))
