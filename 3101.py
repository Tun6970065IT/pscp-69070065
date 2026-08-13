"""waterstatus"""

temp = int(input())
unit = input().lower()
if unit == "c":
    if not temp:
        print("solid")
    elif temp == 100:
        print("gas")
    elif 0 < temp < 100:
        print("liquid")
elif unit == "f":
    if temp == 32:
        print("solid")
    elif temp == 212:
        print("gas")
    elif 32 < temp < 212:
        print("liquid")
