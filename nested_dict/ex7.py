test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]

s = set()
for dic in test_list:
   for val in dic.values():
      s.add(val)
print(s)

