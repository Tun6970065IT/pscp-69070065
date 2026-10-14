"""Shorten"""

def main():
    """Shorten"""
    list_num = []
    while True:
        num = int(input())
        if num == -1:
            break
        list_num.append(num)
    if not list_num:
        print()
    else:
        result = []
        start = list_num[0]
        end = list_num[0]
        for i in range(1 , len(list_num)):
            if list_num[i] == end + 1:
                end = list_num[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}-{end}")
                start = list_num[i]
                end = list_num[i]
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")
        print(", ".join(result))

main()
