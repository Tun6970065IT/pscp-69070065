"""นก"""

def bird():
    """นก"""
    n = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    i = 0
    while i < n:
        ok = True
        if i > 0 and h[i - 1] > h[i]:
            ok = False
        if i < n - 1 and h[i + 1] > h[i]:
            ok = False
        if ok:
            ans += 1
        i += 1
    print(ans)

bird()
