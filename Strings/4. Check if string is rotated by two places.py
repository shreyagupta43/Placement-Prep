def isRotated(s,p):
    n=len(s)
    x=s+s
    if(len(s)==len(p)):
        if(n==1 or n==2) and (s==p):
            return True
        
        
        if(p==x[2:n+2]) or (p==x[n-2:n+4]):
            return True
    return False