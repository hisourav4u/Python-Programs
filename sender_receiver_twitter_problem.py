def fn(l, threshold):
    storeMap={}
    for item in l:
        item_split=item.split(" ")
        sender=item_split[0]
        recipient=item_split[1]
        if sender==recipient:
            if sender in storeMap:
                storeMap[sender]+=1
            else:
                storeMap[sender]=1
        else:
            if sender in storeMap:
                storeMap[sender]+=1
            else:
                storeMap[sender]=1
            
            if recipient in storeMap:
                storeMap[recipient]+=1
            else:
                storeMap[recipient]=1
    
    print(storeMap)
    op=[]
    
    for key in storeMap.keys():
        if storeMap[key]>=threshold:
            op.append(key)
            
    return op

n=int(input())
l=[]
for i in range(n):
    l.append(input())
threshold=int(input())
print(fn(l,threshold))
