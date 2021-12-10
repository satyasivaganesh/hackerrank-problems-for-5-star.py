def migratoryBirds(arr):
    dict={}
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    x=0
    for j in dict:
        if dict[j]>x:
            x=dict[j]
    t=[]
    for j in dict:
        if dict[j]==x:
            t+=[j]
    return min(t)

        
