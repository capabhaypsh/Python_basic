'''Object-like attribute access for nested dictionary
'''

data = {'a': 'aval', 'b': {'b1':{'b2a':{'b3a':'b3aval','b3b':'b3bval'},'b2b':'b2bval'}} }

# print(data['b']['b1']['b2b'])
for i in data:
    # print(data[i])
    data['a'] = 'new'
    print(data)


    