'''
i = 0
while i < 100
    print(i)
    i = i + 5
'''

'''
for i in range(0,100,5)
    print(i)
'''

def fibonacciFinder (max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k
    return("Fibonacci!!")

def primeFinder (max):
    for i in range(2,max):
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            print(i)
    return(max)

def triangleArea(base, height):
    area = base*height/2
    return area
triangleArea(3,6)

n = 5
m = 5
i = 0
areaList = [0]*n*m
for b in range(0,n):
    for h in range(0,m):
        areaList[i] = triangleArea(b,h)
        i = i + 1

print(areaList)