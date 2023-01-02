class G():
    def m(self):
        print("G")

class F(G):
    def m(self):
        print("F")
        super().m()

class E(G):
    def m(self):
        print("E")
        super().m()

class D(G):
    def m(self):
        print("D")
        super().m()

class C(E):
    def m(self):
        print("C")
        super().m()

class B(D, E, F):
    def m(self):
        print("B")
        super().m()

class A(B, C):
    def m(self):
        print("A")
        super().m()

x = A()
y = A.mro()
print(y)
x.m()        