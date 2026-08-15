"""passnotpass"""

subject = int(input())
total = 0
min_score = 100
for _ in range(subject):
    score = int(input())
    total += score
    if score < min_score:
        min_score = score

average = total / subject

if average >= 60 and min_score >= 50:
    print(f"{average:.1f}")
    print("PASS")
else:
    print(f"{average:.1f}")
    print("FAIL")
