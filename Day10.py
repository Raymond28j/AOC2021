with open('c:/Users/raymo/Desktop/Python scripts/Day10.txt') as myfile:
    mylist = [[x for i,x in enumerate(line)] for line in myfile]

def isleft(a):
    if a=='(':
        return 1
    elif a=='[':
        return 2
    elif a=='{':
        return 3
    elif a=='<':
        return 4
    else:
        return 0

def isright(a):
    if a==')':
        return -1
    elif a==']':
        return -2
    elif a=='}':
        return -3
    elif a=='>':
        return -4
    else:
        return 0

mysum=0
mystack=[]
# myerror=[[] for x in range(mylist)]
myerror=[]
myresult = 0

""" #part1
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        mylist[i][j] = isleft(mylist[i][j]) + isright(mylist[i][j])
        if mylist[i][j] > 0:
            mystack.append(mylist[i][j])
        if mylist[i][j] < 0:
            if j==0:
                myerror.append(mylist[i][j])
                break
            elif mylist[i][j] + mystack[-1] != 0:
                    myerror.append(mylist[i][j])
                    break
            else:
                mystack.pop(-1)
    mystack=[]

myresult = myerror.count(-1)*3 + myerror.count(-2)*57 + myerror.count(-3)*1197 + myerror.count(-4)*25137 """

myadd=[]
myflag = 0
#part 2
for i in range(len(mylist)):
    # print(myflag)
    for j in range(len(mylist[i])):
        mylist[i][j] = isleft(mylist[i][j]) + isright(mylist[i][j])
        if mylist[i][j] > 0:
            mystack.append(mylist[i][j])
        if mylist[i][j] < 0:
            if j==0:
                # myerror.append(mylist[i][j])
                myflag = 1
                break
            elif mylist[i][j] + mystack[-1] != 0:
                    # myerror.append(mylist[i][j])
                    myflag = 1
                    break
            else:
                mystack.pop(-1)
    # print(mystack,myflag)
    if myflag == 0:
        mystack.reverse()
        myadd.append(mystack)
    mystack=[]
    myflag = 0

myfinal = []

for i in range(len(myadd)):
    for j in range(len(myadd[i])):
        myresult = myresult * 5 +  myadd[i][j]
    myfinal.append(myresult)
    myresult = 0

myfinal.sort()

print(myadd)
# print(myerror)
print(myfinal[len(myfinal)//2])


