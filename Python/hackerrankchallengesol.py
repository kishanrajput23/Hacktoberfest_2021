def sumsDivisibleByK( a,n, k):
    count = [0]*k
    for i in range (n):
        count[a[i] % k] += 1
    sum = count[0] * (count[0] - 1)/2;
    i = 1
    while(i<=k//2 and i != (k-i)):
        sum+=count[i]*count[k-i]
        i+=1
    if(k%2==0):
        sum+=(count[k//2]*(count[k//2]-1)/2);
    return int(sum)
a = [1, 2, 3, 4, 5]
k = 2
n = len(a)
print(sumsDivisibleByK(a, n, k))


