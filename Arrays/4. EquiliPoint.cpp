int find_afterSum(long long array[], int n)
{
    int afSum=0;
    for (int i=0;i<n;i++)
    {
        afSum= afSum + array[i];
    }
    return afSum;
}
int equilibriumPoint(long long a[], int n)
{
    int bsum=0;
    if(n==1)
        return 1;
    int asum= find_afterSum(a,n);

    for(int i=0;i<n;i++)
    {
        asum= asum-a[i];
        if(asum==bsum)
            return i+1;
        else
            bsum= bsum + a[i];
    }
    return -1;
    

    
}
