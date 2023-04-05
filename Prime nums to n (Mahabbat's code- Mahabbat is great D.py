def sadelistqaytar(n):
    reqemler = set(range(n,1,-1))
    sadeler = []
    while reqemler:
        k = reqemler.pop()
        sadeler.append(k)
        reqemler.difference_update(set(range(k*2,n+1,k)))
    return sadeler
k = int(input("Ededi daxil edin: "))

with open('1.txt','w') as f:
    f.writelines(str(max(sadelistqaytar(k))))

