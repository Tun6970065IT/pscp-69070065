"""buphesunniwas"""

def main():
    """destiny"""
    bf = input().strip()
    gf = input().strip()
    if len(bf) < len(gf):
        shorts,_ = bf,gf
        i = 0
        while len(bf) < len(gf):
            bf += shorts[i % len(shorts)]
            i+=1
    elif len(gf) < len(bf):
        shorts = gf
        i = 0
        while len(gf) < len(bf):
            gf += shorts[i % len(shorts)]
            i += 1
    love = set("love")
    bup = ""
    for x , y in zip(bf , gf):
        if x.lower() in love or y.lower() in love:
            bup += "w"
        else:
            bup += "$"
    w_count = bup.count("w")
    mrun = 0
    run = 0
    for c in bup:
        if c == "w":
            run += 1
            mrun = max(mrun , run)
        else:
            run = 0
    if w_count % 2 == 1:
        bup += str(mrun)
    else:
        if mrun < 2:
            bup += "#"

    print(bup)

main()
