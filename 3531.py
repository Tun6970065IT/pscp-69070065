"""missingnum"""

def main():
    """missingnum"""
    n = int(input())
    list_num = []
    while True:
        num = int(input())
        if not num:
            break
        list_num.append(num)
    all_num = set(range(1 , n+1))
    missing = sorted(list(all_num - set(list_num)))
    for i in missing:
        print(i)

main()
