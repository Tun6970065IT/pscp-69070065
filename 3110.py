"""fast sent war"""

locate = input()
locate_split = locate.split(" ")
start = locate_split[0]
stop = locate_split[1]
Weight = float(input())
total = 0
if start == "BKK" and stop == "CNX":
    total = (30 * Weight) + 10
    print(f"{total:.2f}")
elif start == "CNX" and stop == "UBP":
    total = (40 * Weight) + 15
    print(f"{total:.2f}")
elif start == "UBP" and stop == "BKK":
    total = (40 * Weight) + 20
    print(f"{total:.2f}")
elif start == "BKK" and stop == "PKT":
    total = (50 * Weight) + 25
    print(f"{total:.2f}")
elif start == "PKT" and stop == "CNX":
    total = (60 * Weight) + 30
    print(f"{total:.2f}")
elif start == "UBP" and stop == "PKT":
    total = (70 * Weight) + 40
    print(f"{total:.2f}")
else:
    print("Error")
