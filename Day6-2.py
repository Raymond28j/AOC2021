with open('c:/Users/raymo/Desktop/Python scripts/Day6.txt') as myfile:
    for line in myfile:
        mylist = [int(x) for x in line.split()]
# print(mylist)

count = 0
myfishcount = []
myfishvalue = [0,1,2,3,4,5]
myresult = 0

for j in range(max(mylist)+1):
    for i in range(len(mylist)):
        if mylist[i] == j:
            count += 1
    myfishcount.append(count)
    #myfish.insert(0,count)
    count=0
print(myfishcount)


for j in range(256):
    for i in range(1,len(myfishvalue)):
        myfishvalue[i] -= 1
        if myfishvalue[i] < 0:
            myfishcount.append(myfishcount[i])
            myfishvalue.append(8)
            myfishvalue[i] = 6
    if i % 10 == 0:
        for i in range(1,len(myfishvalue)):
            for j in range(i+1,len(myfishvalue)):
                if myfishvalue[i] == myfishvalue[j]:
                    myfishcount[i] = myfishcount[i] + myfishcount[j]
                    myfishvalue.pop(j)
                    myfishcount.pop(j)
                break


for i in range(1,len(myfishvalue)):
    myresult += myfishcount[i]


print(myresult)

