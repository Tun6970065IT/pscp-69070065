"""LastStand"""

def last():
    """LastStand"""
    nums = input().strip()
    no_list = nums.strip("[]")
    real = no_list.split(",")
    for num in real:
        print(num[-1])

last()
