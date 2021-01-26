def leaders(A,n):
    lis=[]
    if(n==1):
        return A[0]
        
    for i in range(n):
        a=0

        for j in range(i+1,n):
            if(A[i]>=A[j]):
                continue
            else:
                a=1
        if a==0:
            lis.append(A[i])
            
    return lis[:]