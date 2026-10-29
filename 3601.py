"""มากี่คน"""

def main():
    """มากี่คน"""
    list_num = []
    while True:
        num = int(input())
        if num < 0:
            break
        num = str(num)
        list_num.append(num)
    men_count = 0
    girl_count = 0
    men = ["1" , "3" , "5" , "7" , "9"]
    girl = ["0" , "2" , "4" , "6" ,"8"]
    for i in list_num:
        if i[-1] in men:
            men_count += 1
        elif i[-1] in girl:
            girl_count += 1
    total = men_count + girl_count
    print(f"{men_count} {girl_count} {total}")

main()
