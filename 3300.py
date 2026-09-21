"""lifebalance"""
def life():
    """find our life balanced"""
    work = int(input())
    hard = 0
    easy = 0
    totalday = 0
    for _ in range(work):
        hour = int(input())
        if hour > 18:
            hard += 1
        else:
            easy += 1
    if not hard:
        totalday = easy
    elif easy >= hard:
        totalday = (hard * 2) + (easy - hard)
        #งานหนัก = ทำงาน2วัน  + งานเบา - งานหนักเพื่อหางานเบาที่เหลือ
    else:
        totalday = (hard *2) - 1
        # -1 คือ งานหนักวันสุดท้ายไม่มีวันพัก
    print(totalday)
life()
