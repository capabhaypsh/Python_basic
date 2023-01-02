a=10
b=5

try:
    d=a/b
    print(d)
    print('Your code execute properly')
except ZeroDivisionError:    
    print('Code not executed properly due to devide by zero')

else:
    print(a*b)
    print('your new line code')

finally:
    print(a**b)
    print('it is also executed properly')
