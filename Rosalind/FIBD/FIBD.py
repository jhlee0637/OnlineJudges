def makeMemo(monthUntil, monthLive):
    memo=[1,1]
    for i in range(2, monthUntil):
        if i<monthLive: #before death start
            death=0
        if i>=monthLive and i-monthLive-1>=0 : #after death start
            death=memo[i-monthLive-1]
        elif i>=monthLive and i-monthLive-1<0: #First death
            death=1
        val=memo[i-1]+memo[i-2]-death
        print(f'i={i} val={memo[i-1]}+{memo[i-2]}-{death}={val}')
        memo.append(val)
    return memo
    
if __name__=="__main__":
    monthUntil=6
    monthLive=3
    print(makeMemo(monthUntil, monthLive))