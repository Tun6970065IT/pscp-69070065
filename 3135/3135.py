"""giftntheef"""

n , k , t = map(int , input().split())

current = 1
ans = 0
for _ in range(1 , n+1):
    if current == t:
        ans = _
        break
    next_per = (current - 1 + k) % n + 1
    if next_per == 1:
        ans = _
        break
    current = next_per
print(ans)
