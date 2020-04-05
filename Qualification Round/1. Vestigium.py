for t in range(int(input())):
    N=int(input())
    m=[]
    for i in range(N):
        m.append(list(map(int,input().split())))
    r=0
    c=0
    d=0
    for i in m:
        if len(set(i))!=N:
            r+=1
    for i in zip(*m):
        if len(set(i))!=N:
            c+=1
    for i in range(N):
        d+=m[i][i]
    print("Case #{t1}: {d1} {r1} {c1}".format(t1=t+1, d1=d, r1=r, c1=c))
