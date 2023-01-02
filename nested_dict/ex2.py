b={"first": {"age": "31", "Salary": "25000"},"second":{"street":"1","Build_no":"second floor one"}}

for i in b:
    for j in b[i]:
        print(j,b[i][j])
        b['first']['Salary'] = 3000
        b['second']['street'] = 2
        print(b)


