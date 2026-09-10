"""inflation"""
def infla():
    """inflation"""
    n = input()
    k = int(input())

    if "." in n:
        first,end = n.split(".")
    else:
        first,end = n,""
    stang = (end + "00")[:2]
    total = int(first) * 100 + int(stang)
    for _ in range(k):
        total = total * 10381 // 10000
    print(f"{total // 100}.{total % 100:02d}")
infla()
