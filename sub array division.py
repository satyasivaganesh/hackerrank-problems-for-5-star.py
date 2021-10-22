def birthday(s, d, m):
    i=0
    c=0
    while i<=n-m:
        y=s[i:i+m]
        print(y)
        x=sum(y)
        print(x)
        if x==d:
            c+=1
        i+=1
    return c
    # Write you
