"""coke"""
def main():
    """coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        print(a * d)
    elif not d:
        print(0)
    else:
        print(a + ((a*(b-1)+c) * (\
    (d - 1) // b )) + (((d-1) % b) * a))
main()
