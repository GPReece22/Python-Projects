from statistics import mean

weathers = []
print("Welcome to the weather station")

try:
    for temps in range(6):
        weathers.append(float(input("Please enter temp " + str(temps + 1))))

    max = max(weathers)
    min = min(weathers)
    avg = sum(weathers) / len(weathers)
    print("max temp is", max)
    print("Min temp is", min)
    print("Avg temp is", round(avg, 2))

except ValueError:
    print("Please enter numbers only")