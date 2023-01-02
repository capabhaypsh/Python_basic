'''Accessing data from nested dict value using for loop'''

# b={"first": {"age": "31", "Salary": "25000"},"second":{"street":"1","Build_no":"second floor one"}}
# for i in b:
#   for j in b[i]:
#    print(j, b[i][j])

# example2 for updatye the data
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for i  in people:
    for j in people[i]:
        # print(j,people[i][j])

        # updating the name value in dict
        people[1]['Name'] = 'abhay'
        people[1]['Age'] = 25
        print(j,people[i][j])




