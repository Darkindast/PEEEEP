f = open('26-peps1.txt')
n,maxx = map(int, f.readline().split())
d =[]
for i in range(n):
    a, b = map(int, f.readline().split())
    d.append([a, b])
    
d.sort(key = lambda x: (-x[0],x[1]))
maxxm = []
summm = d[0][1]
maxxm.append(summm)
for i in range(len(d)-1):
    if d[i][0] != d[i+1][0]:
        if d[i+1][1] +summm <= maxx:
            summm += d[i+1][1]
            maxxm.append(summm)
        else:
            maxxm.append(summm)
    else:
        maxxm.append(summm)  
        
maxxh = []
summh = d[0][0]
maxxh.append(summh)
for i in range(len(maxxm)-1):
    if maxxm[i] != maxxm[i+1]:
        summh += d[i+1][0]
        maxxh.append(summh)
    else:
        maxxh.append(summh)
        
fset = set(maxxh)
print(max(fset), len(fset))

