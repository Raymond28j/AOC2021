mylist = []
with open('c:/Users/raymo/Desktop/Python scripts/Day7.txt') as myfile:
    for line in myfile:
        mylist = [int(x) for x in line.split(",")]


myflag = 0
myresult = 2048//2
myupperb = 2048
# myresult = max(mylist)//2
# myupperb = max(mylist)
mylowerb = 0
myfuel = 0
myfuel1 = 0
myfuel2 = 0

for j in range(len(mylist)):
    # myfuel += abs(myresult - mylist[j])
    myfuel += (abs(myresult - mylist[j]) + 1) * abs(myresult - mylist[j]) //2
print(myfuel)

# for i in range(1,max(mylist)):
for i in range(1,15):
    for j in range(len(mylist)):
        # myfuel1 += abs((myresult + myupperb) //2 - mylist[j])
        myfuel1 += (abs((myresult + myupperb) //2 - mylist[j]) + 1) * abs((myresult + myupperb) //2 - mylist[j]) //2
    print(myfuel1)
    for j in range(len(mylist)):
        # myfuel2 += abs((myresult + mylowerb) //2 - mylist[j])
        myfuel2 += (abs((myresult + mylowerb) //2 - mylist[j]) + 1) * abs((myresult + mylowerb) //2 - mylist[j]) //2
    print(myfuel2)
    if myfuel1 < myfuel:
        mylowerb = mylowerb + 2048//(2**i)
        myresult = (myresult + myupperb) //2
        myfuel = myfuel1
    elif myfuel2 < myfuel:
        myupperb = myupperb - 2048//(2**i)
        myresult = (myresult + mylowerb) //2
        myfuel = myfuel2
    else: 
        mylowerb = mylowerb + 2048//(2**i)//2
        myupperb = myupperb - 2048//(2**i)//2
    if mylowerb>myupperb:
        break
    myfuel1,myfuel2 = 0,0
    # mylowerb = mylowerb + 2048//(4**i)
    # myupperb = myupperb - 2048//(4**i)
    print(mylowerb,myresult,myupperb,myfuel)


print(myresult)
print(myfuel)
# print(2048//2)
# print(max(mylist))
# print(min(mylist))