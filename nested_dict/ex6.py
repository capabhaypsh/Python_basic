# list comprehension
l1= [i for i in range(6)]
print(l1)
l1.append("abhay")
l1.append(1)
l1.extend(['I ne here extended'])
print(l1)
x=l1.count(1)
print(x)
# set comprehension
l2={i for i in range(5)}
print(l2)

# dictionary comprehesion
l3={i:i*2 for i in range(5)}
print(l3)



