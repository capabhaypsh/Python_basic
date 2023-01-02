# merging a dictionary
capital_dict_1 = {"India": "New Delhi",
		          "Pakistan": "Islamabad",
		          "Nigeria": "Abuja",
		          "Zambia": "Lusaka"}

capital_dict_2 = {"Peru": "Lim", 
                  "Ghana": "Accra"}

capital = {**capital_dict_1, **capital_dict_2}
print(capital)

l1=[1,2]
l2=[3,4]
o={*l1,*l2}
print(o)

# create a dict using comprehension method
# From one list:

lst = [0,1,2,3,4,5]
dic = {x : x**2 for x in lst}

print(dic)

# From two parallel lists
Countries  = ["India", "Pakistan", "Nigeria", "Zambia", "Ghana"]
Capitals = ["New Delhi", "Islamabad", "Abuja", "Lukasa", "Accra"]

capital_dict = {key:value for key,value in zip(Countries,Capitals)}
print(capital_dict)


# creating list and dict using comprehension
x = [i for i in range(5)]
y = {i: i**2 for i in range(4)}
print(x)
print(y)



