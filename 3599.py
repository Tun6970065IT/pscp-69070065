"""sumofnum"""

def sum_of_num():
    """sum of num"""
    num = int(input())
    sum_num = 0
    while True:
        another = int(input())
        if another == -1:
            break
        sum_num += another
        if sum_num == num:
            break
    print(sum_num)

sum_of_num()
