class A:
    def adef(self):
        print("hi")

class B(A):
    def bdef(self):
        print("b hello")

class C(A):
    def cdef(self):
        print("c hello")        

class D(B,C):
    def ddef(self):
        print("d hello")
    
obj=D()
obj.ddef()
obj.cdef()

