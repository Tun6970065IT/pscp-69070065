"""array haha"""

def main():
    """array haha"""
    array = []
    for i in range(1,4):
        num = int(input())
        array.append(num)
        print(f"Input number {i} stored.")
    while True:
        menu = int(input())
        if not menu:
            break
        if menu == 1:
            print(f"Original order: {array[0]} {array[1]} {array[2]}")
        elif menu == 2:
            desen = sorted(array , reverse=True)
            print(f"Descending order: {desen[0]} {desen[1]} {desen[2]}")
        elif menu == 3:
            ascen = sorted(array)
            print(f"Ascending order: {ascen[0]} {ascen[1]} {ascen[2]}")

main()
