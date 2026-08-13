"""pod"""

N , K = map(int,input().split())
q = [0] * K

for _ in range(N):
    row = int(input())
    q[row-1] += 1

pod = min(q)
print(N - pod * K)
