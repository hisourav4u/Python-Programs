def fn(ip):
    if ip.isdigit():
        return [int(ip)]
    else:
        results = []
        #print(enumerate(ip))
        for i,c in enumerate(ip):
            #print(i,c)
            if c == "+":
                l = fn(ip[:i])
                r = fn(ip[i+1:])
                results = results+[n+m for n in l for m in r]
            if c == "-":
                l = fn(ip[:i])
                r = fn(ip[i+1:])
                results = results+[n-m for n in l for m in r]
            if c == "*":
                l = fn(ip[:i])
                r = fn(ip[i+1:])
                results = results+[n*m for n in l for m in r]
        return results
        
ip=input()
print(sorted(fn(ip)))
