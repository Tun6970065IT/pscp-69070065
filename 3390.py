"""Array 2D"""

def main():
    """Array 2D"""
    matrix = []
    for _ in range(5):
        row = list(map(int,input().split()))
        matrix.append(row)

    bad_row = -1
    bad_coll = -1
    for i in range(5):
        if sum(matrix[i]) % 2:
            bad_row = i
            break
    for j in range(5):
        coll_sum = sum(matrix[i][j] for i in range(5))
        if coll_sum % 2:
            bad_coll = j
            break
    print(f"{bad_row} {bad_coll}")

main()
