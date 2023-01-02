class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")
class C(B, A):
  pass

c = C()
c.method()


