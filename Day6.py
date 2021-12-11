with open('c:/Users/raymo/Desktop/Python scripts/Day6.txt') as myfile:
    mylist = [[int(x) for x in line.split()] for line in myfile]

""" print(len(mylist))
print(len(mylist)[0]) """

for i in range(1,257):
#for i in range(1,2):
    for j in range(len(mylist[0])):
        if mylist[0][j] == 0:
            mylist[0].append(8)
            mylist[0][j] = 6
        else:
            mylist[0][j] -= 1

#print(mylist)
#print(len(mylist))
print(len(mylist[0]))







