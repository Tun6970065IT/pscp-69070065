"""Bonus"""

po = input()
bonus = 0
po_split = po.split(" ")
postion = po_split[0]
age = int(po_split[1])
salary = int(po_split[2])
if postion == "M":
    if age <= 5:
        bonus = (6/100) * salary + 1500
        print(int(bonus))
    elif 5 < age <= 10:
        bonus = (8/100) * salary + 1500
        print(int(bonus))
    elif age > 10:
        bonus = (10/100) * salary + 1500
        print(int(bonus))
elif postion == "B":
    if age <= 5:
        bonus = (5/100) * salary + 1000
        print(int(bonus))
    elif 5 < age <= 10:
        bonus = (6/100) * salary + 1000
        print(int(bonus))
    elif age > 10:
        bonus = (7/100) * salary + 1000
        print(int(bonus))
elif postion == "G":
    if age <= 5:
        bonus = (4/100) * salary + 500
        print(int(bonus))
    elif 5 < age <= 10:
        bonus = (5/100)*salary + 500
        print(int(bonus))
    elif age > 10:
        bonus = (6/100) * salary + 500
        print(int(bonus))
