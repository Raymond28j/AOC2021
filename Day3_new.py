with open('Day3.txt') as myfile:
    mylist = [[int(x) for x in line.split()] for line in myfile]

count = 0
mycomp = [0 for x in range(len(mylist[0]))]
myone = []
myzero = []
myresult1 = 0
myresult2 = 0
for i in range(len(mylist)):
    if mylist[i][0] == 1:
        count += 1
        myone.append(i)
    else:
        myzero.append(i)
if count >= len(mylist)/2:
    mycomp[0] = 1


# print(count)
count = 0
#most common 
# for i in range(1):
for i in range(len(mylist[0])):
    if mycomp[i] == 1:
        mymost = myone
    else:
        mymost = myzero
    # print(mymost)
    myone = []
    myzero = []
    # print(count)
    # print(myone)
    for j in mymost:
        if mylist[j][i+1] == 1:
            count += 1
            myone.append(j)
            # print(myone)
        else:
            myzero.append(j)
            # print(myzero)
    # print(count)
    if count >= len(mymost)/2:
        mycomp[i+1] = 1
    if len(myone) <= 1 and len(myzero) <= 1:
        if len(myone)>=len(myzero):
            mymost=myone
        else:
            mymost=myzero
        print(mymost)
        break
    count=0

count = 0
mycomp = [0 for x in range(len(mylist[0]))]
myone = []
myzero = []

for i in range(len(mylist)):
    if mylist[i][0] == 1:
        count += 1
        myone.append(i)
    else:
        myzero.append(i)
if count <= len(mylist)/2:
    mycomp[0] = 1

# print(count)
count=0

#least common
for i in range(len(mylist[0])):
    if mycomp[i] == 1:
        myleast = myone
    else:
        myleast = myzero
    # print(myleast)
    myone = []
    myzero = []
    # print(myone)
    for j in myleast:
        if mylist[j][i+1] == 1:
            count += 1
            myone.append(j)
            # print(myone)
        else:
            myzero.append(j)
            # print(myzero)
    if count < len(myleast)/2:
        mycomp[i+1] = 1
    if len(myone) <= 1 and len(myzero) <= 1:
        if len(myone)>len(myzero):
            myleast=myone
        else:
            myleast=myzero
        print(myone,myzero)
        print(myleast)
        break
    count=0

print(mylist[mymost[0]])
print(mylist[myleast[0]])
for i in range(len(mylist[0])):
    myresult1 += 2 ** (len(mylist[0])-i-1) * mylist[mymost[0]][i]
    myresult2 += 2 ** (len(mylist[0])-i-1) * mylist[myleast[0]][i]

print(myresult1)
print(myresult2)
print(myresult1*myresult2)
# print(myone)
