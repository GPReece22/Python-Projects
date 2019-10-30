price_list = []
counter = 0
while counter < 6:
    price = input("please enter the price of sweet" + str(counter + 1))
    if price[-1].lower() in ("p",):
        temp_cleaned = int(price[:-1])
        price_list.append(temp_cleaned)
        counter += 1
    else:
        print("please enter the price of the sweet in pence")
max = max(price_list)
min = min(price_list)
print("The most expensive sweet is", max, "pence")
print("The least expensive sweet is", min, "pence")
avg = sum(price_list) / len(price_list)
rounded = round(avg, 2)
print("The average price of the sweets is", rounded, "pence")
