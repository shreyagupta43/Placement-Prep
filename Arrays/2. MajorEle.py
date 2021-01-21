def majorityElement(A,N):
    lis=[]
    Check=A[0]
    count=1
    MaxCo=1
    A.sort()
    if (N==1):
        return A[0]
        
    for i in range(1,N):
        if(A[i]==Check):
            count= count+1
        else:
            count= 1
            Check=A[i]

            
        if (count>MaxCo):
            MaxCo=count
            MajorEle=A[i]
            
            if (MaxCo > (N//2)):
                return MajorEle
    return -1
            
  