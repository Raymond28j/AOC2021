with open('Day3.txt') as myfile:
    mylist = [[int(x) for x in line.split()] for line in myfile]

count = 0
mycomp = [0 for x in range(len(mylist[0]))]
myrest = []
myresult1 = 0
myresult2 = 0
for i in range(len(mylist)):
    if mylist[i][0] == 1:
        count += 1
        myrest.append(i)
if count > len(mylist)//2:
    mycomp[0] = 1




match = 0
count = 0
row1 = 0
i,j=0,0
for j in range(1,len(mylist[0])):
    for i in range(len(mylist)):
        for k in range(1,j):
            if mylist[i][j-1] == mycomp[j-1]:       #compare previous column with max common bit
                break
            if mylist[i][j] == 1:
                count += 1
            if k == j:
                row1 = i
            
        if count >= len(mylist)//2:
            mycomp[j] = 1
            count = 0               
    if count <= 1:
        break
print(mycomp)

""" for i in range(1,len(mylist[0])):
    mycomp[i] = 0
for i in range(1,len(mylist[0])):
    mycomp[i] = 1 - mycomp[i]
print(mycomp) """

count = 0
row2 = 0
i,j=0,0
#for j in range(1,len(mylist[0])):
for j in range(1):    
    for i in range(len(mylist)):
        if mylist[i][j-1] == (1 - mycomp[j-1]):       #compare previous column with max common bit
            #print(1 - mycomp[j-1])
            row2 = i
            if mylist[i][j] == 1:
                count += 1
        if count > len(mylist)//2:
            mycomp[j] = 1
            count = 0      
    print(j)        
    if count <= 1:
        break



for i in range(len(mylist[0])):
    myresult1 += 2 ** (len(mylist[0])-i-1) * mylist[row1][i]
    myresult2 += 2 ** (len(mylist[0])-i-1) * mylist[row2][i]

print(row1)
print(mylist[row1])
print(myresult1)
print(row2)
print(mylist[row2])
print(myresult2)
print(mylist[6][0])

