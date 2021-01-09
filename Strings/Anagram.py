def isAnagram(a,b):
    
    x= sorted(a)

    y= sorted(b)
   
    if(x==y):
        return True
    else:
        return False

