"""Promotionprice"""
import math
def main():
    """Pro"""
n = input()
n_spilt = n.split(" ")
a = int(n_spilt[0])
b = int(n_spilt[1])
c = int(n_spilt[2])
total = 0
total_price = 0
abc = a + b +c
if abc >= 3 or a >= 3 or b >= 3 or c >= 3:
    total = (a * 25) + (b *40) + (c*55)
    discount = (10/100) * total
    total_price = total - discount
    print(math.floor(int(total_price)))
else:
    total = (a * 25) + (b *40) + (c*55)
    print(math.floor(int(total)))
main()
