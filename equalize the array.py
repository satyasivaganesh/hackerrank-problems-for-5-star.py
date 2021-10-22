def equalizeArray(arr):
    t=[]
    x=1
    for i in arr:
        if i not in t:
            t.append(i)
    for i in t:
        if x<arr.count(i):
            x=arr.count(i)
    return n-x
