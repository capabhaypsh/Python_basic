mylist=[1,3,5,7,8,2,9,0]
mylist.sort()
print('my ascending list',mylist)

mylist.sort(reverse=True)
print('my descending list',mylist)

al = ['a','d','e','c','b']
al.sort(reverse=True)
print('alphabet List in Descending Order: ', al)

al.sort()

print('alphabet List in Ascending Order: ', al)


cities = ['Mumbai', 'London', 'Paris', 'New York']
cities.sort()
print('List in Ascending Order: ', cities)
cities.sort(reverse=True)
print('List in Descending Order: ', cities)
#sort using key as length of the string
cities = ['Mumbai', 'London', 'Paris', 'New York']

cities.sort(key=len)
print('List in Ascending Order of the length: ', cities)
cities.sort(key=len, reverse=True)
print('List in Descending Order of the length: ', cities)

# Sort List of Class Objects
class student:
	name=''
	age=0
	def __init__(self, name, age):
		self.name = name
		self.age = age

s1 = student('Bill', 25)
s2 = student('Steve', 29)
s3 = student('Ravi', 26)

student_list = [s1, s2, s3]
# student_list.sort() # raise an error
student_list.sort(key=lambda s: s.name) # sorts using lambda function
print('Students in Ascending Order:', end=' ')
for std in student_list:
	print(std.name, end=', ')
student_list.sort(key=lambda s: s.name, reverse=True) # sorts using lambda function
print('Students in Descending Order:', end=' ')
for std in student_list:
	print(std.name, end=', ')



