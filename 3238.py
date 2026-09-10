"""elonmuskk"""
def elon():
    """elonmuskk"""
    num , k = input().split()
    num = int(num)
    mid = num // 2 #หาแถวกลาง
    for i in range(num):
        dis = abs(i - mid) #หาระยะห่างจากแถวกลาง
        if k == "#":
            char = "#"
        else:
            char = chr(ord(k) + dis)
        row = ""
        for j in range(num):
            if i == j  or i + j == num -1: #ตำแหน่งcolum
                row += char
            else:
                row += "-"
        print(row)
elon()
