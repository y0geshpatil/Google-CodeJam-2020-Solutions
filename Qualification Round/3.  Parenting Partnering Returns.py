for t in range(int(input())):
    N=int(input())
    s,e=[],[]
    n=[]
    for i in range(N):
        s1,e1=list(map(int,input().split()))
        s.append(s1)
        e.append(e1)
        n.append(i)
    
    a=sorted(zip(s,e,n))
    #print(a)
    c=[]
    j=[]
    l=0
    for i in range(len(a)):
        if a[i][0]>=l:
            j.append(i)
            l=a[i][1]
    l=0
    for i in range(len(a)):
        if a[i][0]>=l and i not in j:
            c.append(i)
            l=a[i][1]
    s=""
    for i in range(N):
        if i in j:
            s=s+'J'
        if i in  c:
            s=s+'C'
    res=[""]*N
    if len(s)!=N:
        res='IMPOSSIBLE'
    else:
        for i in range(N):
            res[a[i][2]]=s[i]
    print("Case #{t1}: {d1}".format(t1=t+1, d1="".join(res)))
