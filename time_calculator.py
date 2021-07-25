def add_time(start, duration, day=False):
    timezone = (start.split(" "))[1]
    finalhour = 0
    finalmin = 0
    finalmin = int(((start.split(" "))[0]).split(":")[1]) + int(duration.split(":")[1])
    day_checker = {"sunday": 0,"monday": 1,"tuesday": 2,"wednesday": 3,"thursday": 4,"friday": 5,"saturday": 6}
    days = [", Sunday",", Monday",", Tuesday",", Wednesday",", Thursday",", Friday",", Saturday"]
    finalday = ""
    days_later = 0
    while finalmin > 59:
        finalhour += 1
        finalmin -= 60
    finalhour = finalhour + int(((start.split(" "))[0]).split(":")[0]) + int(duration.split(":")[0])
    finalhourmodifier = finalhour
    while finalhour > 12:
        finalhour -= 12
    while finalhourmodifier > 11:
        finalhourmodifier -= 12
        timezone = "PM" if timezone == "AM" else "AM"
        days_later += 1
    if days_later % 2 != 0:
        if timezone == "PM":
            days_later -= 1
        else:
            days_later += 1    
    days_later = int(days_later / 2)
    finalhour = str(finalhour)
    finalmin = str(finalmin)
    if len(finalmin) == 1:
        finalmin = "0" + finalmin
    if len(finalmin) == 0:
        finalmin = "00"
    if day:
        day = day.lower()
        currentday = day_checker[day]
        currentday = int(currentday) + days_later
        while int(currentday) >= 7:
            currentday -= 7
        finalday = days[currentday]
    later = " (" + str(days_later) + " days later)"
    if days_later == 1:
        later = " (next day)"
    if days_later == 0:
        later = ""
    new_time = finalhour + ":" + finalmin + " " +timezone + finalday + later
    print(new_time)
    return new_time
add_time()