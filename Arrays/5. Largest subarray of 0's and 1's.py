def maxLen(arr, N):
    
    for i in range(N):
        if arr[i]==0:
             arr[i] = -1  
    
    sum = 0
    equalNo = 0
    dict = {}
    for i in range(N):
        sum = sum + arr[i]
        
        if sum == 0:
            equalNo = i+1
        if sum in dic:
            equalNo = max(i-dict[sum], equalNo)
        else:
            dict[sum] = i
    
    return equalNo 