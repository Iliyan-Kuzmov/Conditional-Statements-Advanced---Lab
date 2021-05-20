dni_prestoi = int(input())
room = input()
ocenka = input()
nostuwki = dni_prestoi - 1
price = 0
if dni_prestoi < 10:
    if room == "room for one person":
        price = 18.00
    elif room == "apartment":
        price = 0.7 * 25.00
    elif room == "president apartment":
        price = 0.9 * 35.00
elif 10 <= dni_prestoi <= 15:
    if room == "room for one person":
        price = 18.00
    elif room == "apartment":
        price = 0.65 * 25.00
    elif room == "president apartment":
        price = 0.85 * 35.00
elif 15 < dni_prestoi:
    if room == "room for one person":
        price = 18.00
    elif room == "apartment":
        price = 0.5 * 25.00
    elif room == "president apartment":
        price = 0.8 * 35.00
price = price * nostuwki
if ocenka == "positive":
    price = price * 1.25
elif ocenka == "negative":
    price = price * 0.9
print(f"{price:.2f}")