class A:
    pass
class B:
    pass
class C(A, B):
    pass
class D(B):
    pass
class E(C,A,D):
    pass

class F(E):
    pass
# f-e-c-a-b-a-d-b-0bjects
#f-e-c-a-d-b-obj

print(F.mro())


