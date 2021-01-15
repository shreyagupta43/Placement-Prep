#With Space Complexity = O(n)
def isRotated(s,p):
    n=len(s)
    x=s+s
    if(len(s)==len(p)):
        if(n==1 or n==2) and (s==p):
            return True
        
        if(p==x[2:n+2]) or (p==x[n-2:n+4]):
            return True
    return False

    #With Space Complexity = O(1)
    def isRotated(s,p):
    n = len(s)
    
    if (len(s)==len(p)):
        if (n==1 or n==2) and s==p:
            return True
        if n>2:
            if ((s[2:] == p[:n-2] or s[:n-2] == p[2:])):
                return True

    return False