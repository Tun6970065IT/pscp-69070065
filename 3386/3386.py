"""Dupiclate"""

def main():
    """Dupiclate"""
    group1 = int(input())
    group2 = int(input())
    list_mem = []
    dupi = []
    seen = []
    for _ in range(group1 + group2):
        member = input()
        list_mem.append(member)
    for i in list_mem:
        if i in seen:
            if i not in dupi:
                dupi.append(i)
        else:
            seen.append(i)
    dupi.sort(reverse=True)
    if not dupi:
        print("Nope")
    else:
        for j in dupi:
            print(j)
main()
