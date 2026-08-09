"""test score"""

test_score = int(input())
max_score = -1
count = 0
for i in range(test_score):
    score = int(input())
    if score > max_score:
        max_score = score
        count = 1
    elif score == max_score:
        count += 1
    i += 1
print(max_score)
print(count)
