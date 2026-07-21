"""docstring"""

def main():
    """rabbit"""
    veget = input()
    veget_split = veget.split(" ")
    a = int(veget_split[0])
    b = int (veget_split[1])
    c = int(veget_split[2])
    solve = (a*10) + (b*25) + (c*3)
    print(solve)

main()
