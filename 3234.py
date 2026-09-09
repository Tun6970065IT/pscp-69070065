"""chrismast"""
def hoho():
    """chrismast"""
    fcolor , amount = input().split()
    amount = int(amount)
    if fcolor == "R":
        num = 0
    elif fcolor =="G":
        num = 1
    else:
        num = 2
    for _ in range(amount):
        color = (num + _) % 3

        if not color:
            print("Red",end="")
        elif color == 1:
            print("Green",end="")
        else:
            print("Blue",end="")
        if _ < amount-1:
            print(" ", end="") # เว้นวรรคระหว่างคำ (ยกเว้นตัวสุดท้าย)
    print() # ขึ้นบรรทัดใหม่ตอนพิมพ์จบ
hoho()
