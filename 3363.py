"""ไข้หวัดกระต่ายสายพันธ์ใหม่"""

def main():
    """ไข้หวัดกระต่ายสายพันธ์ใหม่"""
    def rabbit(a):
        """ไข้หวัดกระต่าย"""
        if not a:
            return 100
        if a == 1:
            return 60
        if a == 2:
            return 20
        return 0
    r , c = map(int, input().split())
    br , bc = map(int, input().split())
    n = int(input())

    r_infect = []
    for _ in range(n):
        a , b = map(int, input().split())
        r_infect.append((a , b))

    safe = 0
    rabbit_risk = 0
    for i in range(r):
        for j in range(c):
            best = 0
            for (a , b) in r_infect:
                a = max(abs(i-a) , abs(j - b))
                best = max(best , rabbit(a))
            if not best:
                safe += 1
            if i == br and j == bc:
                rabbit_risk = best

    print(safe)
    print(str(rabbit_risk) + "%")

main()
