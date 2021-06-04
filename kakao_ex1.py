# 제 1회
# 1등 500만원
# ~3등 300만원
# ~6등 200만원
# ~10등 50만원
# ~15등 30만원
# ~21등 10만원

cp1 = [[1,5000000],[3,3000000],[6,2000000],[10,500000],[15,300000],[21,100000]]

# 제 2회
# 1등 512만원
# ~3등 256만원
# ~7등 128만원
# ~15등 64만원
# ~31등 32만원

cp2 =[[1,5120000],[3,2560000],[7,1280000],[15,640000],[31,320000]]
    
T=int(input())
t=0
abs=[]

while(t<T):
    a,b =map(int,input().split(' '))
    abs.append([a,b])
    t=t+1

# print(abs)

for i in abs:
    if i[0] != 0 and i[0]<=21:
        for j in cp1:
            if i[0] <= j[0]:
                areword = j[1]
                break
    else:
        areword = 0
    if i[1] != 0 and i[1] <= 31:
        for k in cp2:
            if i[1] <= k[0]:
                breword = k[1]
                break
    
    else:
        breword = 0
        
#     print(areword,"+",breword,"=",areword + breword)
    print(areword + breword)