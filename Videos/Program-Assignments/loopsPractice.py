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

i = 0
j = 1
k = 0
while i < 100:
    print(k)
    k = i + j
    i = j
    j = k

for i in range(1,1000):
    for j in range (2,i):
        if i % j == 0:
            break
    else:
        print(i)


