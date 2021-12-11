with open('c:/Users/raymo/Desktop/Python scripts/Day1.txt') as myfile:
    mylist = [[int(x) for x in line.split()] for line in myfile]

i=0
count=0
#part1
#for i in range(len(mylist)-1):
#    if mylist[i+1] > mylist[i]:
#        count += 1

for i in range(len(mylist)-3):
    if mylist[i+3] > mylist[i]:
        count += 1
print(count)






