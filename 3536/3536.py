"""isprime_large"""

def main():
    """isprime_large"""
    num = int(input())
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        i = 2
        while i ** 2 <= num:
            if not num % i:
                is_prime =False
                break
            i += 1
    if is_prime:
        print("YES")
    else:
        print("NO")

main()
