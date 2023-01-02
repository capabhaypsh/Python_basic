class A:
    pass
class B:
    pass
class C:
    pass
class D(A, C, B):
    pass
class E(D, A, B, C):
    pass

print(E.mro())


# Class Sequence should same otherwise error will come

