for t in range(int(input())):
    mo=list(map(int,list(input())))
    m=mo[:]
    s=[""]*(len(m)+1)
    for l in range(len(m)):
        for j in range(len(m),l,-1):
            mi=min(m[l:j])
            m[l:j]=list(map(lambda x: x-mi,m[l:j]))
            for k in range(mi):
                s[l]=s[l]+"("
                s[j]=s[j]+")"
    print("Case #{t1}:".format(t1=t+1),end=" ")
    print(s[0],end="")
    for i in range(len(mo)):
        print(str(mo[i])+s[i+1],end="")
    print()
