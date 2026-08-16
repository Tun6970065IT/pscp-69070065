"""trianggle"""
n = int(input())

for _ in range(1,n+1):
    if _ == 1:
        print("0")
    elif _ == n:
        print("0" * _)
    else:
        print("0"+"1"*(_ - 2)+"0")
        