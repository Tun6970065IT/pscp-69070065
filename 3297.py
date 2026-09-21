"""MOVIETICKET"""

maxt = int(input())
while maxt > 0:
    age , amount = map(int , input().split())
    if age < 15:
        print("-1")
    elif amount > maxt:
        print("-2")
    else:
        if 15 <= age <= 22:
            PRICE = 120
        elif age >= 60:
            PRICE = 75
        else:
            PRICE = 150

        total = PRICE * amount
        maxt -= amount
        print(f"{total} {maxt}")
