"""BASICATM"""

ex = int(input())
if ex <= 0 or ex % 100:
    print("ERROR")
else:
    bank1000 = ex // 1000
    ex %= 1000
    bank500 = ex // 500
    ex %= 500
    bank100 = ex // 100
    ex %= 100
    if bank1000> 0:
        print(f"1000 = {bank1000}")
    if bank500 > 0:
        print(f"500 = {bank500}")
    if bank100 > 0:
        print(f"100 = {bank100}")
