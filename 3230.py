"""hotelno13"""

def hotel():
    """hotelno13"""
    num = int(input())
    snum = f"{num:05d}" #ถ้าไม่ครบ5จะเติม0ด้านหน้า
    palinnum = snum[::-1]
    n1,n2,n3,n4,n5 = int(snum[0]),int(snum[1]),int(snum[2]),int(snum[3]),int(snum[4])
    first = ""
    if n1 > 5:
        first = "9"
    elif n2 > 5:
        first = "10"
    elif n3 > 5:
        first = "11"
    elif n4 > 5:
        first = "12"
    elif n5 > 5:
        first = "14"
    else:
        first = "13"
    sec = ""
    if snum == palinnum:
        if n1 + n5 > 5:
            sec = "1"
        elif n2 * n4 > 5:
            sec = "2"
        else:
            sec = "0"
    else:
        round_num = int((n1 / n5) + 0.5) if n5 else 0 # กัน5เป็น0ไม่งั้นติดzerodivisionerror
        if round_num > 5:
            sec = "1"
        elif n2 - n5 > 5:
            sec = "2"
        else:
            sec = "0"
    third = ""
    if n1 + n2 + n3 + n4 + n5 > 25:
        third = "1"
    elif n1 * n2 * n3 * n4 * n5 > 55:
        third = "2"
    else:
        third = "0"
    print(first + sec + third)
hotel()
