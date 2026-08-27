"""ramen"""

size , teste = input().split()
topping = input().split()

price = 0

if size == "S":
    if teste == "R":
        price = 60
    elif teste == "T":
        price = 80
elif size == "M":
    if teste =="R":
        price = 80
    elif teste == "T":
        price = 100
elif size == "L":
    if teste == "R":
        price = 100
    elif teste == "T":
        price = 120

topping_type = topping[0]
if topping_type != "N":
    amount = int(topping[1])
    if amount > 0:
        if topping_type == "P":
            price += amount * 15
        elif topping_type == "E":
            price += amount * 10

print(price)
