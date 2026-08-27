"""สหกรณ์โรงเรียน"""

m = input()
amount = int(input())
beforedis = 0
total = 0
equa = 0
for _ in range(1,amount+1):
    price = float(input())
    beforedis += price

if m == "Y":
    equa = int(beforedis * 95 + 0.5)
    total = equa / 100
    print(f"{total:.2f}")
elif m == "N":
    if beforedis >= 500:
        equa = int(beforedis * 97 + 0.5)
        total = equa / 100
        print(f"{total:.2f}")
    else:
        print(f"{beforedis:.2f}")
else:
    print(f"{beforedis:.2f}")
