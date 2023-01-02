l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
# l1.append(l2)
print(l1)
l1.extend(l2)
print(l1)
x=list(zip(l1,l2))
print(x)
l1z,l2z=zip(*x)
print("l1 values: %d", l1z)
print("l1 values: %s", l2z)
print(l2z)


x='abhay'
z=x.split('a')
print(x)


