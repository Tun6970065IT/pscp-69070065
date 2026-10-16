"""ส่งต่อ"""

def main():
    """ส่งต่อ"""
    n , s = map(int , input().split())

    Next = [0] * (n+1)
    for i in range(1 , n+1):
        Next[i] = int(input())

    visit = [False] * (n+1)
    count = 0
    current = s

    while current and not visit[current]:
        visit[current] = True
        count += 1
        current = Next[current]

    print(count)

main()
