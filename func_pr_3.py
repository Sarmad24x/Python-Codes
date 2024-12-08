def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
ans=sum(5)
print(ans)