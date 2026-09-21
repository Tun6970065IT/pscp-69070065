"""BIGFRAMEEEEEE"""

def frame():
    """drawbigframee"""
    word = []
    long = 0
    for i in range(5):
        a = input().strip()
        word.append(a)
        if len(a) > long:
            long = len(a)
    print("*" * (long + 4))
    for i in word:
        print("* "+ i + (" " * (long - len(i))) +" *")
    print("*" * (long + 4))

frame()
