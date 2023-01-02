# 0,1,1,2,3,5,8...
def fib(n):
    if n==0:
        return 0

    elif n==1 or n==2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))

# hello print with decorator

def mydef(func):
    def newdef():
        print("**********")
        func()
        print("**********")
    return newdef
@mydef
def hello():
    print("hello abhay")
hello()

#square value with list comprehension
l1=[x**2 for x in range(5)]
print(l1)

# even number
l2=[x for x in range(5) if x%2==0]
print(l2)


la=[1,2,3,4]
lb=[4,3,2,1]

m=list(map(lambda n,m:n+m,la,lb))
print(m)

f=list(filter(lambda n:n-2,la))
print(f)

# list_comprhension prime number 1,3,5,7,13...
s= [x for x in range(1, 20) if all(x % y != 0 for y in range(2, x))]
print(s)

for i in range(5):
    if i==3:
        continue
        # pass
        # break
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1 : : 2])

