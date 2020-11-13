speed_limit = 50
mph_list = []
kph_list = []
speeders = 0
heavy_vehicles = 0
light_vehicles = 0
private_cars = 0
counter = 0

while 1:
    speed = input("Next reading: ")
    if speed.upper() == "END" and counter == 0:
        print("You have not entered any speeds")
        counter += 1
    elif speed.upper() == "END":
        break
    elif speed[0].upper() in ("H", "L", "C") and 0 < int(speed[1:]) < 100:
        speed_value = int(speed[1:])
        kph_value = speed_value * 1.609
        mph_list.append(speed_value)
        kph_list.append(kph_value)
        counter += 1
        if speed[0].upper() == "H":
            heavy_vehicles += 1
        elif speed[0].upper() == "L":
            light_vehicles += 1
        elif speed[0].upper() == "C":
            private_cars += 1
        if speed_value > speed_limit:
            speeders += 1
    else:
        print("please enter the correct format")

print("Total number of vehicles seen:", counter)

heavy_percent = round((heavy_vehicles / counter) * 100, 2)
print("Number of heavy goods vehicles seen:", heavy_vehicles, heavy_percent, "%")

light_percent = round((light_vehicles / counter) * 100, 2)
print("Number of light good vehicles seen:", light_vehicles, light_percent, "%")

private_percent = round((private_cars / counter) * 100, 2)
print("Number of private cars seen:", private_cars, private_percent, "%")

print("Highest speed seen:", max(mph_list), "MPH", max(kph_list), "KPH")
print("Lowest speed seen:", min(mph_list), "MPH", min(kph_list), "KPH")

avg_mph = round(sum(mph_list) / len(mph_list), 2)
avg_kph = round(sum(kph_list) / len(kph_list), 2)
print("Average speed seen:", avg_mph, "MPH", avg_kph, "KPH")

speeders_percent = (speeders/counter)*100
print("Speed limit violations:", speeders, round(speeders_percent, 2), "%")
