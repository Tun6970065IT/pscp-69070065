"""giraffe"""

def main():
    """giraffe"""
    n = int(input())
    list_g = []
    for _ in range(n):
        g = int(input())
        list_g.append(g)
    if n == 1:
        print(1)
        return

    count = 0
    if list_g[0] > list_g[1]:
        count +=1
    for i in range(1 , n-1):
        if list_g[i] > list_g[i-1] and list_g[i] > list_g[i + 1]:
            count += 1
    if list_g[-1] > list_g[-2]:
        count +=1
    print(count)

main()
