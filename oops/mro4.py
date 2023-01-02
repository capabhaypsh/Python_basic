class A:
  def method(self):
    print("A.method() called")

class B(A):
  def method(self):
    print("B.method() called")
    # pass
b = B()
# b.method()

print(B.mro())