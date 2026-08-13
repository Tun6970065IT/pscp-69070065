"""taxi"""

km = int(input())
if km == 1:
    print("35")
elif 1 < km <= 10:
    print(30 + (km * 5))
elif km > 10:
    print(30 + (km *5) + (km * 8))