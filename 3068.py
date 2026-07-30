"""ปีอธิกสุรทิน"""

year = int(input())
if year == "1500":
    print("yes")
if year > 1582:
    if year % 4 == 0:
        print("yes")
    elif year % 4 != 0:
        print("no")
    elif year % 100 == 0:
        print("no")
elif year < 1582:
    print("no")