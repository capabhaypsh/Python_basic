ls=[1,2,3,4,4,5,6,7]
lb=[]
lc=[]
for i in ls:
    if i%2==0:
        lb.append(i)
    else:
        lc.append(i)
print(lb)    
print(lc)    
lb.extend(lc)
print(ls)
print(lb)
#above example ,filter even and odd from list and seperate even and odd in list
x=sum(ls)
print(x)
###############
que=[2,1,4,7,9,0]
c=que.index(0)
print(c)
##########
listOfStrings = ['One', 'Two', 'Three']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)

# List Of Integers to a String
listOfNumbers = [1, 2, 3]
strOfNumbers = ''.join(str(i) for i in listOfNumbers)
print(strOfNumbers)





