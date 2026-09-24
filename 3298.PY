"""BUUAHRABBIT"""

def rabbit():
    """rabbitBUU"""
    text = input().strip().upper()
    Umax = 0
    Unow = 0
    bhave = False
    for char in text:
        if char =="B":
            bhave = True
            Unow = 0
        elif char =="U" and bhave:
            Unow += 1
            if Unow >= 2 and Unow > Umax:
                Umax = Unow
        else:
            bhave = False
            Unow = 0
    if Umax >= 2:
        print(f"Yes {Umax}")
        return
    elif "B" in text:
        whereB = text.find("B")
        result = text[:whereB + 1] + "U" * (len(text) - whereB -1)
        #เปลี่ยนตัวอักษรหลังBเป็น U โดยตัวอักษรก่อนหน้าเป็นเหมือนเดิม
        print(result)
        return
    else:
        no_b = "BUU" * len(text)
        print(no_b[:len(text)])
rabbit()
