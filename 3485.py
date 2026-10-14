"""รหัสไม่ซ้ำ"""

def password():
    """รหัสไม่ซ้ำ"""
    _ = input()
    Pass = list(map(int,input().split()))
    only_pass = []
    for i in Pass:
        if Pass.count(i) == 1:
            only_pass.append(i)
    only_pass.sort()
    print(*only_pass)

password()
