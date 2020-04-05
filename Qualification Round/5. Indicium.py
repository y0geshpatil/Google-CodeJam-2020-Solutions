
def fillRemaining(i, j, n,mat): 
    x = 2

    for k in range(i + 1,n): 
        mat[k][j] = x
        x+=1
    for k in range(i): 
        mat[k][j] = x
        x+=1

def constructMatrix(n,mat): 

    
    for _ in range(n):
        t=[]
        for _ in range(n):
            t.append(0)
        mat.append(t)
    right = n - 1
    left = 0; 
    for i in range(n): 
        if (i % 2 == 0): 
            mat[i][right] = 1 
            fillRemaining(i, right, n,mat)
            right-=1
        else: 
            mat[i][left] = 1
            fillRemaining(i, left, n,mat)
            left+=1
    return mat

##above function for Construct a unique matrix n x n for an input n from https://www.geeksforgeeks.org/



from itertools import permutations
for t in range(int(input())):
    n,k=list(map(int,input().split()))
    #fuu(n)
    mat=[]
    mat=constructMatrix(n,mat)
    #print(mat)
    no=list(permutations([i for i in range(n)]))
    
    '''for i in range(n):
            for j in range(n):
                print(mat[i][j],end=" ")
            print()'''
    f=0
    for v in no:
        t1=[]
        for i in v:
            t2=[]
            for j in range(n):
                t2.append(mat[i][j])
            t1.append(t2)
        res=0
        print(t1)
        for i in range(len(t1)):
            res=res+t1[i][i]
        #print(res)
        if k==res:
            f=1
            print("Case #{t1}: POSSIBLE".format(t1=t+1))
            for i in t1:
                  for j in i:
                      print(j,end=" ")
                  print()
            break
    if f==0:
        print("Case #{t1}: IMPOSSIBLE".format(t1=t+1))
    
