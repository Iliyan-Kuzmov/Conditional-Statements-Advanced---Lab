hour = int(input())
day = str(input())
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if hour != 10 and hour != 11 and hour != 12 and hour != 13 and hour != 14 and hour != 15 and hour != 16 and hour != 17 and hour != 18:
        print("closed")
    else:
        print("open")
if day == "Sunday":
    print("closed")