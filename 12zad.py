city = str(input())
sales = float(input())
c = 0
if city == "Sofia" or city == "Varna" or city == "Plovdiv":
    if city == "Sofia":
        if 0 <= sales <= 500:
            c = 5
        elif 500 < sales <= 1000:
            c = 7
        elif 1000 < sales <= 10000:
            c = 8
        elif 10000 < sales:
            c = 12
    elif city == "Varna":
        if 0 <= sales <= 500:
            c = 4.5
        elif 500 < sales <= 1000:
            c = 7.5
        elif 1000 < sales <= 10000:
            c = 10
        elif 10000 < sales:
            c = 13
    elif city == "Plovdiv":
        if 0 <= sales <= 500:
            c = 5.5
        elif 500 < sales <= 1000:
            c = 8
        elif 1000 < sales <= 10000:
            c = 12
        elif 10000 < sales:
            c = 14.5
    else:
        print("-0.00")
    commision = c/100 * sales
    print(f"{commision:.2f}")
else:
    print("error")
