test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]

s = set()
for dic in test_list:
   for val in dic.values():
      s.add(val)
print(s)


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# static
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
# dynamic
dic={}
for i in (dic1,dic2,dic3):
  dic.update(i)
print(dic)
