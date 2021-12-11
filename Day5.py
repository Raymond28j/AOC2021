#print("YOYOYOLO")


mylist = []
myboard = [[0 for x in range(1000)] for y in range(1000)] 
#myfile = open('Day5.txt')
with open('Day5.txt') as myfile:
    mylist = [[int(x) for x in line.split()] for line in myfile]

i=0
for i in range(500):
    if mylist[i][0] == mylist[i][2]:
        ii = min(mylist[i][1],mylist[i][3])
        while ii <= max(mylist[i][1],mylist[i][3]):
            myboard[mylist[i][0]][ii] += 1
            ii += 1


    elif mylist[i][1] == mylist[i][3]:
        ii = min(mylist[i][0],mylist[i][2])
        while ii <= max(mylist[i][0],mylist[i][2]):
            myboard[ii][mylist[i][1]] += 1
            ii += 1

    else:
        if (mylist[i][1] - mylist[i][3])/(mylist[i][0] - mylist[i][2]) > 0:
            xx = min(mylist[i][0],mylist[i][2])
            yy = min(mylist[i][1],mylist[i][3])
            while xx <= max(mylist[i][0],mylist[i][2]):
                myboard[xx][yy] += 1
                xx += 1
                yy += 1
        else:
            xx = min(mylist[i][0],mylist[i][2])
            yy = max(mylist[i][1],mylist[i][3])
            while xx <= max(mylist[i][0],mylist[i][2]):
                myboard[xx][yy] += 1
                xx += 1
                yy -= 1

    i += 1

#calculate number of 1s
count = 0
for x in range(1000):
    for y in range(1000):
        if myboard[x][y] >=2:
            count += 1

print(count)
#x,y = 0,0
#for x in range(1):
#    for y in range(4):
#        print(mylist[x][y])
#print(mylist[1][1])

#print(mylist[1][0],mylist[1][1],mylist[1][2],mylist[1][3])
#print(mylist[499])