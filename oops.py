class A:
    print("hi")

class B(A):
    print("hi")
    # pass
class C(A):
    pass
x=C()
print(x)

class demo():
    def __init__(self,name,age):
      super().__init__(name,age)
z=demo('abhay','22')
# z.new()


