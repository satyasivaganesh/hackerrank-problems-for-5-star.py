def viralAdvertising(n):
    x=n
    s=2
    y=2
    for i in range(1,x):
        n=y*3
        y=n//2
        s=s+y
    return s
        
