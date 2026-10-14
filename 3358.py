"""pig"""

def ppiigg():
    """pig"""
    n = int(input())
    w = list(map(int,input().split()))
    result = []
    for i in range(n):
        result.append(max(w[i*2] , w[i*2+1]))
    if n == 1:
        print(max(result))
    else:
        print(" + ".join(map(str,result)) , "=" , sum(result))

ppiigg()
