"""GCD_N"""
import math
def main():
    """GCD_N"""
    n = int(input())
    list_num = []
    for _ in range(n):
        num = int(input())
        list_num.append(num)
    ans = list_num[0]
    for i in list_num[1:]:
        ans = math.gcd(ans , i)
    print(ans)
main()
