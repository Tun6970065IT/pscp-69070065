"""Sqfree"""

def main():
    """Sqfree"""
    num = int(input())
    count = 0
    for i in range(1 , num+1):
        sqfree = True
        j = 2
        while j ** 2 <= i:
            if not i % ( j ** 2):
                sqfree = False
                break
            j += 1
        if sqfree:
            count +=1
    print(count)

main()
