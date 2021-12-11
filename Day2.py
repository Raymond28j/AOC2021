with open('Day2.txt') as myfile:
    mylist = [[x for x in line.split()] for line in myfile]

x,y=0,0
#part 1
""" for i in range(len(mylist)):
#for i in range(11):
    mylist[i][1]=int(mylist[i][1])
    if mylist[i][0] == 'forward':
        x += mylist[i][1]
    elif mylist[i][0] == 'up':
        y -= mylist[i][1]
    else:
        y += mylist[i][1]
#    print(mylist[i]) """

#part 2
aim = 0
for i in range(len(mylist)):
#for i in range(11):
    mylist[i][1]=int(mylist[i][1])
    if mylist[i][0] == 'forward':
        x += mylist[i][1]
        y += mylist[i][1] * aim
    elif mylist[i][0] == 'up':
        aim -= mylist[i][1]
    else:
        aim += mylist[i][1]


print(x,y,x*y)
#print(len(mylist))
#print(mylist[999])

