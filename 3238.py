"""elonmuskk"""
def elon():
    """elonmuskk"""
    num , k = input().split()
    num = int(num)
    for _ in range(1,num+1):
        if k == "#":
            if _ == num:
                print("#" + "-"*(_-2)+ "#")
elon()