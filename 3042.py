"""divide10"""

n = int(input())
result = ""
for _ in range(n,-1,-1):
    if not _ %10:
        result += str(_) + " "
print(result)
