"""jumpfrog"""
def frog():
    """jumpfrog"""
    x , y = map(int , input().split())
    jump = 0
    goal = 0
    for _ in range(x,0,-2):
        goal += _
        jump +=1
        if goal >= y:
            break
    if goal >= y:
        print(jump)
    else:
        print("-1")
frog()
