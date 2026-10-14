"""พูดจาภาษากระต่าย"""

def rabbit():
    """พูดจาภาษากระต่าย"""
    word = input().strip().upper()
    n = len(word)

    if all(c in "IT" for c in word):
        print("unknown" , n)
    else:
        good = 0
        cur = 0
        for i , c in enumerate(word):
            p = word[i -1] if i > 0 else""

            if c == "A" and p not in ("R" , "A"):
                print("no" , i)
                break
            if p == "R" and c!= "A":
                print("no" , i)
                break
            if p == "B" and c not in("I" , "T"):
                print("no" , i)
                break

            if c == "A":
                cur +=1
                good = max(good , cur)
            else:
                cur = 0
        else:
            if word[-1] in ("R" , "B"):
                print("no" , n)
            else:
                print("yes" , good)

rabbit()
