a=10
b=0

try:
    d=a/b
    print(d)
    print('Your code execute properly')
except (ZeroDivisionError ,NameError) as obj:    
    print(obj)

else:
    print(a*b)
    print('your new line code')

# finally:
#     print(a**b)
#     print('it is also executed properly')
