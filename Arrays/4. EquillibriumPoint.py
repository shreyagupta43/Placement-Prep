def equilibriumPoint(A, N):
    if(N==1):
        return 1
    bsum=0

    asum=sum(A)
    for i in range(N):
        asum= asum-A[i]
        if(bsum==asum):
            return i+1
        else:
            bsum= bsum+A[i]
    return -1
        