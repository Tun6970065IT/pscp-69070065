"""smart trash collector"""

def trash():
    """trash collector"""
    n = int(input())
    for _ in range(n):
        t1 , t2 , t3 = map(float,input().split())
        total = t1 + t2 + t3
        collect = [f"{total:.1f}"]
        if total > 50:
            collect.append("Overloaded")
        if t1 > 20:
            collect.append("Check Type Plastic")
        if t2 > 20:
            collect.append("Check Type Can")
        if t3 > 20:
            collect.append("Check Type Glass")

        print(", ".join(collect))

trash()
