with open('Day11.txt') as myfile:
    mylist = [[int(x) for x in line.split()] for line in myfile]
with open('Day11.txt') as myfile:    
    flashlist = [[0 for x in line.split()] for line in myfile]


def flash(mlist,flist,in1,in2):
    flist[in1][in2] = 1
    mlist[in1][in2] = 0
    # if flist[i][j]==1:
    #     pass
    # else:
    for x in range(3):
        for y in range(3):
            if in1-1+x < 0 or in2-1+y < 0 or in1-1+x >= len(mlist) or in2-1+y >= len(mlist[0]):
                pass
            elif flist[in1-1+x][in2-1+y] == 1:
                pass
            else:
                mlist[in1-1+x][in2-1+y] += 1
                if mlist[in1-1+x][in2-1+y] >= 10:
                    flash(mylist,flashlist,in1-1+x,in2-1+y)
                # print(x,y,in1-1+x,in2-1+y)


count = 0
myday = 0
for days in range(1000):
    for x in range(len(mylist)):
        for y in range(len(mylist[0])):
            if flashlist[x][y] == 1:
                pass
            else:
                mylist[x][y] += 1
                if mylist[x][y] >= 10:
                    flash(mylist,flashlist,x,y)
    for x in range(len(flashlist)):
        count += flashlist[x].count(1)
    if sum([i.count(1) for i in flashlist]) == 100:
        myday = days +1
        break
    # for x in range(len(mylist)):
    #     print(flashlist[x])
    flashlist=[[0 for y in range(len(mylist[0]))] for x in range(len(mylist))]

# t1=[[1,1,1],[1,1,1],[1,1,1]]
# t2=[[0,0,0],[0,0,0],[0,0,0]]
# a,b=1,1
# flash(t1,t2,a,b)
# print(t1,t2)
print('\n')
for x in range(len(mylist)):
    print(mylist[x])
print(count)
print(myday)
