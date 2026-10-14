"""hint"""

def main():
    """hint"""
    op1 , num1 = input().split()
    op2 , num2 = input().split()
    op3 , num3 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    for hun in range(10):
        if op3 == "==" and hun != num3:
            continue
        if op3 == "!=" and hun == num3:
            continue
        if op3 == ">" and hun <= num3:
            continue
        if op3 == "<" and hun >= num3:
            continue
        if op3 == ">=" and hun < num3:
            continue
        if op3 == "<=" and hun > num3:
            continue
        for ten in range(10):
            if op2 == "==" and ten != num2:
                continue
            if op2 == "!=" and ten == num2:
                continue
            if op2 == ">" and ten <= num2:
                continue
            if op2 == "<" and ten >= num2:
                continue
            if op2 == ">=" and ten < num2:
                continue
            if op2 == "<=" and ten > num2:
                continue
            for i in range(10):
                if op1 == "==" and i != num1:
                    continue
                if op1 == "!=" and i == num1:
                    continue
                if op1 == ">" and i <= num1:
                    continue
                if op1 == "<" and i >= num1:
                    continue
                if op1 == ">=" and i < num1:
                    continue
                if op1 == "<=" and i > num1:
                    continue
                print(f"{hun}{ten}{i}")

main()
