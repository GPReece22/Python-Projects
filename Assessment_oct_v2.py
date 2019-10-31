
# % for number of each type of vehicle
# validity for speeds 0-99
# deal with no data inputs
# tidy up, too much repetition

speed_limit = 50
speed_list = []
speeders = 0
heavy_vehicles = 0
light_vehicles = 0
private_cars = 0
counter = 0

while 1:
    speed = input("Next reading: ")
    if speed.upper() == "END":
        break
    elif speed[0].upper() in ("H", "L", "C"):
        speed_value = int(speed[1:])
        speed_list.append(speed_value)
        counter += 1
        if speed_value > speed_limit:
            speeders += 1
# is there a way to do this without 3 seperate if statements, looks a bit messy
        if speed[0].upper == "H":
            heavy_vehicles += 1
        elif speed[0].upper == "L":
            light_vehicles += 1
        elif speed[0].upper == "C":
            private_cars += 1
    else:
        print("please enter the correct format")

# could this be done in 1 loop rather than 3 seperate blocks??
print("Total number of vehicles seen:", counter)

heavy_percent = (heavy_vehicles / counter) * 100
print("Number of heavy goods vehicles seen:", heavy_vehicles, ".", heavy_percent, "%")

light_percent = (light_vehicles / counter) * 100
print("Number of light good vehicles seen:", light_vehicles, light_percent, "%")

private_percent = (private_cars / counter) * 100
print("Number of private cars seen:", private_cars, private_percent, "%")

# do these kph calcs on whole list to simplify??
max_mph = max(speed_list)
max_kph = round(max_mph * 1.609)
print("Highest speed seen:", max_mph, "MPH", max_kph, "KPH")

min_mph = min(speed_list)
min_kph = round(min_mph * 1.609)
print("Lowest speed seen:", min_mph, "MPH", min_kph, "KPH")

avg_mph = round(sum(speed_list) / len(speed_list),2)
avg_kph = round(avg_mph * 1.609, 2)
print("Average speed seen:", avg_mph, "MPH", avg_kph, "KPH")

speeders_percent = (speeders/counter)*100
print("Speed limit violations:", speeders, "(", round(speeders_percent, 2), "%) of vehicles seen")
