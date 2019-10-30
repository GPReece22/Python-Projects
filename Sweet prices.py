sweets = []

try:
    for count in range(6):
        sweets = (input("Please enter the price of sweet " + str(count + 1)))
    if sweets[-1].lower() in ("p",):
        price = int(sweets[:-1])
        sweets.append(price)
    else:
        print("Please enter a value in pence")

    max = max(price)
    min = min(price)
    avg = sum(price) / len(price)
    print("max temp is", max)
    print("Min temp is", min)
    print("Avg temp is", round(avg, 2))

except ValueError:
    print("Please enter numbers only")
